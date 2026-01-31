import streamlit as st
import pandas as pd
import joblib
from dash.healthscore import calculate_health_score

# ==============================
# Streamlit Page Setup
# ==============================
st.set_page_config(page_title="SME Financial Health", layout="wide")
st.title("📊 SME Financial Health Assessment")

# ==============================
# Load Model & Artifacts
# ==============================
model = joblib.load("financial_health_model.pkl")
le = joblib.load("label_encoder.pkl")
feature_cols = joblib.load("feature_columns.pkl")

st.sidebar.info("Upload SME financial data CSV to assess financial health.")

# ==============================
# File Upload
# ==============================
uploaded_file = st.file_uploader("Upload CSV", type=["csv"])

if uploaded_file:
    df = pd.read_csv(uploaded_file)
    df.columns = df.columns.str.strip()

    # ==============================
    # 1️⃣ Feature Engineering (SAFE)
    # ==============================

    # Cost Ratio
    if "Cost_Ratio" not in df.columns:
        if {"COGS", "Revenue"}.issubset(df.columns):
            df["Cost_Ratio"] = df["COGS"] / df["Revenue"].replace(0, 1)
        else:
            st.error("❌ Missing COGS or Revenue to compute Cost_Ratio")
            st.stop()

    # Profit Margin (FIX FOR YOUR ERROR)
    if "Profit_Margin" not in df.columns:
        if {"NetProfit", "Revenue"}.issubset(df.columns):
            df["Profit_Margin"] = df["NetProfit"] / df["Revenue"].replace(0, 1)
        else:
            st.warning("⚠️ Profit_Margin cannot be computed (NetProfit/Revenue missing)")
            df["Profit_Margin"] = 0  # safe fallback

    # ==============================
    # 2️⃣ Feature Validation
    # ==============================
    missing_features = [f for f in feature_cols if f not in df.columns]
    if missing_features:
        st.error(f"❌ Missing required model features: {missing_features}")
        st.stop()

    # ==============================
    # 3️⃣ Model Input Alignment
    # ==============================
    X = df[feature_cols]

    # ==============================
    # 4️⃣ Predictions
    # ==============================
    preds = model.predict(X)
    probs = model.predict_proba(X).max(axis=1)

    df["Health_Status"] = le.inverse_transform(preds)
    df["Confidence"] = probs.round(2)

    # ==============================
    # 5️⃣ Health Score Calculation
    # ==============================
    df["Health_Score"] = df.apply(calculate_health_score, axis=1)

    # ==============================
    # 6️⃣ KPIs
    # ==============================
    col1, col2, col3 = st.columns(3)
    col1.metric("Avg Health Score", round(df["Health_Score"].mean(), 1))
    col2.metric("Healthy SMEs", (df["Health_Status"] == "Healthy").sum())
    col3.metric("Risky SMEs", (df["Health_Status"] == "Risky").sum())

    # ==============================
    # 7️⃣ Visuals
    # ==============================
    st.subheader("📋 SME Financial Assessment")
    st.dataframe(df, use_container_width=True)

    st.subheader("📊 Avg Health Score by Status")
    st.bar_chart(df.groupby("Health_Status")["Health_Score"].mean())

    if {"Revenue", "NetProfit"}.issubset(df.columns):
        st.subheader("📈 Revenue vs Net Profit")
        st.line_chart(df[["Revenue", "NetProfit"]])
