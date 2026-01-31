import pandas as pd
import numpy as np

# ==============================
# 1️⃣ LOAD RAW DATA (SAFE MODE)
# ==============================
df = pd.read_csv("financial_data.csv")

# 🚨 IF CSV LOADED AS SINGLE COLUMN, FIX IT
if df.shape[1] == 1:
    print("⚠️ CSV loaded as single column — fixing format")

    df = df.iloc[:, 0].str.split(",", expand=True)
    df.columns = [
        "TransactionID",
        "TransactionDate",
        "OrderID",
        "Revenue",
        "COGS",
        "GrossProfit",
        "OperatingExpenses",
        "NetProfit"
    ]

print("✅ Dataset Loaded Correctly")
print("Shape:", df.shape)
print(df.head())

# ==============================
# 2️⃣ DATA TYPE CONVERSION
# ==============================
df["TransactionDate"] = pd.to_datetime(df["TransactionDate"], errors="coerce")

numeric_cols = [
    "Revenue",
    "COGS",
    "GrossProfit",
    "OperatingExpenses",
    "NetProfit"
]

for col in numeric_cols:
    df[col] = pd.to_numeric(df[col], errors="coerce")

# ==============================
# 3️⃣ HANDLE MISSING VALUES
# ==============================
df[numeric_cols] = df[numeric_cols].fillna(0)
df["TransactionDate"] = df["TransactionDate"].fillna(method="ffill")

# ==============================
# 4️⃣ REMOVE DUPLICATES
# ==============================
df.drop_duplicates(inplace=True)

# ==============================
# 5️⃣ FEATURE ENGINEERING
# ==============================
df["Profit_Margin"] = np.where(
    df["Revenue"] > 0,
    df["NetProfit"] / df["Revenue"],
    0
)

df["Cost_Ratio"] = np.where(
    df["Revenue"] > 0,
    df["OperatingExpenses"] / df["Revenue"],
    0
)

df["Loss_Flag"] = (df["NetProfit"] < 0).astype(int)

# ==============================
# 6️⃣ TIME FEATURES
# ==============================
df["Year"] = df["TransactionDate"].dt.year
df["Month"] = df["TransactionDate"].dt.month
df["Day"] = df["TransactionDate"].dt.day

# ==============================
# 7️⃣ OUTLIER HANDLING
# ==============================
for col in numeric_cols:
    q1 = df[col].quantile(0.25)
    q3 = df[col].quantile(0.75)
    iqr = q3 - q1
    lower = q1 - 1.5 * iqr
    upper = q3 + 1.5 * iqr
    df[col] = df[col].clip(lower, upper)

# ==============================
# 8️⃣ NORMALIZATION
# ==============================
from sklearn.preprocessing import MinMaxScaler

scaler = MinMaxScaler()
df[numeric_cols] = scaler.fit_transform(df[numeric_cols])

# ==============================
# 9️⃣ SAVE OUTPUT
# ==============================
df.to_csv("processed_data.csv", index=False)

print("\n✅ PREPROCESSING COMPLETED SUCCESSFULLY")
print("📁 Output saved as processed_data.csv")
print("Final shape:", df.shape)
