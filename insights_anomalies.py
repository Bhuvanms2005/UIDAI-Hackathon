import pandas as pd

df = pd.read_csv("aadhaar_cleaned.csv")
df["date"] = pd.to_datetime(df["date"])

monthly = df.groupby(["year", "month"])["total_enrolment"].sum().reset_index()
monthly["year_month"] = pd.to_datetime(
    monthly["year"].astype(str) + "-" + monthly["month"].astype(str) + "-01"
)

mean_val = monthly["total_enrolment"].mean()
std_val = monthly["total_enrolment"].std()

high_anomalies = monthly[monthly["total_enrolment"] > mean_val + std_val]
low_anomalies = monthly[monthly["total_enrolment"] < mean_val - std_val]

total_enrolment = df["total_enrolment"].sum()
age_0_5 = df["age_0_5"].sum()
age_5_17 = df["age_5_17"].sum()
age_18 = df["age_18_greater"].sum()

state_summary = df.groupby("state")["total_enrolment"].sum().reset_index()
top_states = state_summary.sort_values(by="total_enrolment", ascending=False).head(5)

print("\nKEY INSIGHTS")
print("------------")
print(f"Total Aadhaar enrolments analysed: {int(total_enrolment):,}")
print(f"Adult (18+) enrolments dominate with {(age_18/total_enrolment)*100:.1f}% share")
print(f"Child enrolments (0–17) contribute {((age_0_5+age_5_17)/total_enrolment)*100:.1f}% of total")
print(f"Top 5 states contribute {(top_states['total_enrolment'].sum()/total_enrolment)*100:.1f}% of total enrolments")

print("\nHIGH ENROLMENT MONTHS (Anomalies)")
print("--------------------------------")
print(high_anomalies[["year_month", "total_enrolment"]])

print("\nLOW ENROLMENT MONTHS (Anomalies)")
print("-------------------------------")
print(low_anomalies[["year_month", "total_enrolment"]])
