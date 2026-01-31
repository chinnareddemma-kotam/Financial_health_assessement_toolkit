from fastapi import FastAPI, UploadFile, File, Depends
from fastapi.middleware.cors import CORSMiddleware
from sqlalchemy.orm import Session
from datetime import datetime
import pandas as pd
import joblib
import os

from database.database import SessionLocal, engine
from database.models import Base, SMESnapshot

# =========================
# Optional Gemini Import
# =========================
try:
    from google import genai
    GEMINI_AVAILABLE = True
except:
    GEMINI_AVAILABLE = False

# =========================
# FastAPI Setup
# =========================
app = FastAPI(title="SME Financial Health API")

app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

# =========================
# Create Tables
# =========================
Base.metadata.create_all(bind=engine)

# =========================
# DB Dependency
# =========================
def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()

# =========================
# Load ML Artifacts
# =========================
model = joblib.load("financial_health_model.pkl")
feature_cols = joblib.load("feature_columns.pkl")

# =========================
# Gemini Client
# =========================
class GeminiClient:
    def __init__(self):
        api_key = os.getenv("GEMINI_API_KEY")
        if not api_key or not GEMINI_AVAILABLE:
            self.enabled = False
            return
        self.client = genai.Client(api_key=api_key)
        self.model = "gemini-1.5-flash"
        self.enabled = True

    def generate_insights(self, summary: dict) -> str:
        if not self.enabled:
            return None

        prompt = f"""
You are an SME financial advisor.

Portfolio Summary:
{summary}

Provide:
1. Overall financial health
2. Key risks
3. Actionable recommendations
"""
        response = self.client.models.generate_content(
            model=self.model,
            contents=prompt
        )
        return response.text

gemini = GeminiClient()

# =========================
# Health Logic
# =========================
def calculate_health_score(row):
    score = 0
    pm = row.get("Profit_Margin", 0)
    cr = row.get("Cost_Ratio", 1)

    score += 35 if pm > 0.2 else 25 if pm > 0.1 else 15
    score += 35 if cr < 0.6 else 25 if cr < 0.8 else 15
    score += 30

    return min(score, 100)

def assign_health_status(score):
    if score >= 85:
        return "Healthy"
    elif score >= 60:
        return "Moderate"
    return "Risky"

# =========================
# Fallback Recommendations
# =========================
def fallback_ai_insights(summary: dict) -> str:
    score = summary.get("avg_health_score", 0)

    if score >= 85:
        status = "STRONG"
        actions = [
            "Maintain cost discipline",
            "Reinvest profits into growth",
            "Expand cautiously",
            "Monitor margins regularly"
        ]
    elif score >= 60:
        status = "MODERATE"
        actions = [
            "Reduce operating expenses",
            "Improve receivable collections",
            "Renegotiate vendor contracts",
            "Increase profit margins"
        ]
    else:
        status = "AT RISK"
        actions = [
            "Immediate cost reduction",
            "Improve liquidity",
            "Restructure debts",
            "Avoid high-risk spending"
        ]

    return f"""
FINANCIAL HEALTH REPORT
----------------------
Overall Status : {status}
Average Score  : {score}

RECOMMENDATIONS
---------------
• {actions[0]}
• {actions[1]}
• {actions[2]}
• {actions[3]}
"""

# =========================
# Predict API
# =========================
@app.post("/predict")
async def predict(file: UploadFile = File(...), db: Session = Depends(get_db)):
    df = pd.read_csv(file.file)
    df.columns = df.columns.str.strip()

    # Feature engineering (safe)
    if "Cost_Ratio" not in df.columns and {"COGS", "Revenue"}.issubset(df.columns):
        df["Cost_Ratio"] = df["COGS"] / df["Revenue"].replace(0, 1)

    if "Profit_Margin" not in df.columns and {"NetProfit", "Revenue"}.issubset(df.columns):
        df["Profit_Margin"] = df["NetProfit"] / df["Revenue"].replace(0, 1)

    X = df[feature_cols].fillna(0)
    probs = model.predict_proba(X).max(axis=1)

    df["Health_Score"] = df.apply(calculate_health_score, axis=1)
    df["Health_Status"] = df["Health_Score"].apply(assign_health_status)
    df["Confidence"] = probs.round(2)

    summary = {
        "avg_health_score": round(df["Health_Score"].mean(), 1),
        "healthy": int((df["Health_Status"] == "Healthy").sum()),
        "moderate": int((df["Health_Status"] == "Moderate").sum()),
        "risky": int((df["Health_Status"] == "Risky").sum()),
    }

    ai_insights = gemini.generate_insights(summary) or fallback_ai_insights(summary)

    for _, row in df.iterrows():
        db.add(SMESnapshot(
            transaction_id=row.get("TransactionID"),
            revenue=row.get("Revenue"),
            profit_margin=row.get("Profit_Margin"),
            cost_ratio=row.get("Cost_Ratio"),
            health_score=row["Health_Score"],
            health_status=row["Health_Status"],
            confidence=row["Confidence"],
            insight=ai_insights
        ))

    db.commit()

    return {
        "summary": summary,
        "ai_insights": ai_insights,
        "data": df.to_dict(orient="records")
    }

# =========================
# History API
# =========================
@app.get("/history")
def history(db: Session = Depends(get_db)):
    return db.query(SMESnapshot)\
        .order_by(SMESnapshot.created_at.desc())\
        .limit(50).all()
