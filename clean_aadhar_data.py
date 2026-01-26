import pandas as pd
df = pd.read_csv("aadhaar_monthly_enrolment_all_states.csv")

print("Raw dataset loaded")
print("Initial shape:", df.shape)
required_columns = [
    "date",
    "state",
    "district",
    "pincode",
    "age_0_5",
    "age_5_17",
    "age_18_greater"
]

missing_cols = set(required_columns) - set(df.columns)
if missing_cols:
    raise ValueError(f"Missing columns in dataset: {missing_cols}")

print("All required columns present")

df["date"] = pd.to_datetime(
    df["date"],
    dayfirst=True,
    errors="coerce"
)

df = df[df["date"].notna()]

age_columns = ["age_0_5", "age_5_17", "age_18_greater"]

for col in age_columns:
    df[col] = pd.to_numeric(df[col], errors="coerce")

df[age_columns] = df[age_columns].fillna(0)

df["state"] = df["state"].astype(str).str.strip().str.title()
df["district"] = df["district"].astype(str).str.strip().str.title()


df["total_enrolment"] = (
    df["age_0_5"] +
    df["age_5_17"] +
    df["age_18_greater"]
)

df["year"] = df["date"].dt.year
df["month"] = df["date"].dt.month
df = df[df["total_enrolment"] >= 0]

print("Final shape after cleaning:", df.shape)
print("Number of states:", df["state"].nunique())
print("Date range:",
      df["date"].min().date(),
      "to",
      df["date"].max().date()
)
df.to_csv("aadhaar_cleaned.csv", index=False)

print("Cleaned dataset saved as aadhaar_cleaned.csv")
