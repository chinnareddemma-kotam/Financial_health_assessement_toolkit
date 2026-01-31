# ==============================
# SME Financial Health Model Training (Updated)
# ==============================

import pandas as pd
import numpy as np
import joblib
from sklearn.model_selection import train_test_split
from sklearn.ensemble import RandomForestClassifier
from sklearn.preprocessing import LabelEncoder
from sklearn.metrics import classification_report, accuracy_score

# ==============================
# 1️⃣ LOAD DATA
# ==============================
df = pd.read_csv("processed_data.csv")
print("✅ Dataset loaded:", df.shape)

# Strip column names to avoid KeyErrors
df.columns = df.columns.str.strip()
print("Columns:", df.columns.tolist())

# ==============================
# 2️⃣ HANDLE MISSING VALUES
# ==============================
# Define feature columns
feature_cols = ["Revenue", "COGS", "OperatingExpenses", "GrossProfit", "Cost_Ratio"]

# Fill missing numeric values with 0
for col in feature_cols:
    if col not in df.columns:
        if col == "Cost_Ratio" and "COGS" in df.columns and "Revenue" in df.columns:
            df["Cost_Ratio"] = df["COGS"] / df["Revenue"].replace(0, 1)
            print("✅ Computed missing Cost_Ratio")
        else:
            raise KeyError(f"❌ Missing required column: {col}")
df[feature_cols] = df[feature_cols].fillna(0)

# ==============================
# 3️⃣ CREATE TARGET LABELS
# ==============================
def create_health_label(row):
    if row["NetProfit"] < 0:
        return "Risky"
    elif row["Profit_Margin"] < 0.20:
        return "Moderate"
    else:
        return "Healthy"

df["Financial_Health"] = df.apply(create_health_label, axis=1)

print("\n📊 Class Distribution:")
print(df["Financial_Health"].value_counts())

# ==============================
# 4️⃣ ENCODE TARGET
# ==============================
le = LabelEncoder()
df["Health_Label"] = le.fit_transform(df["Financial_Health"])
print("✅ Target encoding complete. Classes:", le.classes_)

# ==============================
# 5️⃣ FEATURE SELECTION
# ==============================
X = df[feature_cols]
y = df["Health_Label"]

# ==============================
# 6️⃣ TRAIN-TEST SPLIT
# ==============================
X_train, X_test, y_train, y_test = train_test_split(
    X, y,
    test_size=0.25,
    random_state=42,
    stratify=y
)

print(f"✅ Training samples: {X_train.shape[0]}, Test samples: {X_test.shape[0]}")

# ==============================
# 7️⃣ MODEL TRAINING
# ==============================
model = RandomForestClassifier(
    n_estimators=300,
    max_depth=12,
    class_weight="balanced",
    random_state=42
)

model.fit(X_train, y_train)
print("✅ RandomForest model trained.")

# ==============================
# 8️⃣ EVALUATION
# ==============================
y_pred = model.predict(X_test)
y_prob = model.predict_proba(X_test).max(axis=1)

print("\n📈 Model Evaluation:")
print("Accuracy:", accuracy_score(y_test, y_pred))
print("\nClassification Report:")
print(classification_report(y_test, y_pred, target_names=le.classes_))

# ==============================
# 9️⃣ FEATURE IMPORTANCE
# ==============================
importances = pd.Series(
    model.feature_importances_,
    index=feature_cols
).sort_values(ascending=False)

print("\n💡 Feature Importance:")
print(importances)

# ==============================
# 🔟 SAVE MODEL, ENCODER & FEATURE COLUMNS
# ==============================
joblib.dump(model, "financial_health_model.pkl")
joblib.dump(le, "label_encoder.pkl")
joblib.dump(feature_cols, "feature_columns.pkl")  # <--- NEW
print("\n💾 Saved files:")
print("✔ financial_health_model.pkl")
print("✔ label_encoder.pkl")
print("✔ feature_columns.pkl")