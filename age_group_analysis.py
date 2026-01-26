import pandas as pd
import matplotlib.pyplot as plt
from matplotlib.ticker import FuncFormatter

df = pd.read_csv("aadhaar_cleaned.csv")

age_summary = {
    "Age 0-5": df["age_0_5"].sum(),
    "Age 5-17": df["age_5_17"].sum(),
    "Age 18+": df["age_18_greater"].sum()
}

age_df = pd.DataFrame(list(age_summary.items()), columns=["Age Group", "Total Enrolment"])

total = age_df["Total Enrolment"].sum()
age_df["Percentage"] = (age_df["Total Enrolment"] / total) * 100

def comma_format(x, pos):
    return f"{int(x):,}"

plt.figure(figsize=(8, 6))
plt.bar(age_df["Age Group"], age_df["Total Enrolment"])
plt.gca().yaxis.set_major_formatter(FuncFormatter(comma_format))

for i, row in age_df.iterrows():
    plt.text(
        i,
        row["Total Enrolment"],
        f'{int(row["Total Enrolment"]):,}\n({row["Percentage"]:.1f}%)',
        ha="center",
        va="bottom",
        fontsize=10
    )

plt.title("Aadhaar Enrolment by Age Group")
plt.xlabel("Age Group")
plt.ylabel("Total Enrolments")
plt.tight_layout()
plt.show()

print("\nAge Group Enrolment Summary:")
print(age_df)
