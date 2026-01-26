import pandas as pd
import matplotlib.pyplot as plt
from matplotlib.ticker import FuncFormatter

df = pd.read_csv("aadhaar_cleaned.csv")

state_summary = (
    df.groupby("state")["total_enrolment"]
    .sum()
    .reset_index()
    .sort_values(by="total_enrolment", ascending=False)
    .sort_values(by="total_enrolment", ascending=False)
    .reset_index(drop=True)
)

top_states = state_summary.head(10)
bottom_states = state_summary.tail(10)
middle_states = state_summary.iloc[10:-10]
middle_states_selected = middle_states.sort_values(
    by="total_enrolment", ascending=False
).head(10)
def comma_format(x, pos):
    return f"{int(x):,}"

plt.figure(figsize=(12, 6))
plt.bar(top_states["state"], top_states["total_enrolment"])
plt.gca().yaxis.set_major_formatter(FuncFormatter(comma_format))
for i, v in enumerate(top_states["total_enrolment"]):
    plt.text(i, v, f"{v:,}", ha="center", va="bottom", fontsize=9)
plt.title("Top 10 States by Aadhaar Enrolment")
plt.xlabel("State")
plt.ylabel("Total Enrolments")
plt.xticks(rotation=45, ha="right")
plt.tight_layout()
plt.show()

plt.figure(figsize=(12, 6))
plt.bar(middle_states_selected["state"], middle_states_selected["total_enrolment"])
plt.gca().yaxis.set_major_formatter(FuncFormatter(comma_format))
for i, v in enumerate(middle_states_selected["total_enrolment"]):
    plt.text(i, v, f"{v:,}", ha="center", va="bottom", fontsize=9)
plt.title("Middle States by Aadhaar Enrolment")
plt.xlabel("State")
plt.ylabel("Total Enrolments")
plt.xticks(rotation=45, ha="right")
plt.tight_layout()
plt.show()

plt.figure(figsize=(12, 6))
plt.bar(bottom_states["state"], bottom_states["total_enrolment"])
plt.gca().yaxis.set_major_formatter(FuncFormatter(comma_format))
for i, v in enumerate(bottom_states["total_enrolment"]):
    plt.text(i, v, f"{v:,}", ha="center", va="bottom", fontsize=9)
plt.title("Bottom 10 States by Aadhaar Enrolment")
plt.xlabel("State")
plt.ylabel("Total Enrolments")
plt.xticks(rotation=45, ha="right")
plt.tight_layout()
plt.show()

print("\nState-wise Enrolment Summary (Top 10):")
print(top_states)
print("\nMiddle States Enrolment Summary:")
print(middle_states_selected)
print("\nState-wise Enrolment Summary (Bottom 10):")
print(bottom_states)
