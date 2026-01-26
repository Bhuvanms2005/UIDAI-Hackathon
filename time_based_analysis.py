import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
from matplotlib.ticker import FuncFormatter

df = pd.read_csv("aadhaar_cleaned.csv")
df["date"] = pd.to_datetime(df["date"])

monthly = df.groupby(["year", "month"])["total_enrolment"].sum().reset_index()
monthly["year_month"] = pd.to_datetime(monthly["year"].astype(str) + "-" + monthly["month"].astype(str) + "-01")

yearly = df.groupby("year")["total_enrolment"].sum().reset_index()

def comma_format(x, pos):
    return f"{int(x):,}"

plt.figure(figsize=(12, 6))
plt.plot(monthly["year_month"], monthly["total_enrolment"], marker="o")
plt.gca().yaxis.set_major_formatter(FuncFormatter(comma_format))
for x, y in zip(monthly["year_month"], monthly["total_enrolment"]):
    plt.text(x, y, f"{y:,}", ha="center", va="bottom", fontsize=9)
plt.title("Monthly Aadhaar Enrolment Trend")
plt.xlabel("Time")
plt.ylabel("Total Enrolments")
plt.grid(True)
plt.tight_layout()
plt.show()

plt.figure(figsize=(8, 5))
plt.plot(yearly["year"], yearly["total_enrolment"], marker="o")

ticks = np.arange(yearly["year"].min(), yearly["year"].max() + 0.21, 0.2)
plt.xticks(ticks)

plt.title("Yearly Aadhaar Enrolment Trend")
plt.xlabel("Year")
plt.ylabel("Total Enrolments")
plt.grid(True)
plt.tight_layout()
plt.show()

print("\nMonthly Enrolment Summary:")
print(monthly[["year_month", "total_enrolment"]])

print("\nYearly Enrolment Summary:")
print(yearly)
