import requests
import pandas as pd

API_KEY = "579b464db66ec23bdd000001b47cf35ff53a46907d925889e42bec80"
RESOURCE_ID = "ecd49b12-3084-4521-8f7e-ca8bf72069ba"

BASE_URL = f"https://api.data.gov.in/resource/{RESOURCE_ID}"

all_records = []
limit = 1000
offset = 0

print("Starting data fetch...")

while True:
    params = {
        "api-key": API_KEY,
        "format": "json",
        "limit": limit,
        "offset": offset
    }

    response = requests.get(BASE_URL, params=params)

    if response.status_code != 200:
        print("Error:", response.status_code)
        break

    data = response.json()
    records = data.get("records", [])

    if not records:
        break

    all_records.extend(records)
    offset += limit
    print(f"Fetched {len(all_records)} records so far...")

df = pd.DataFrame(all_records)

print("\nFetch complete")
print("Total records fetched:", len(df))
print("Number of states:", df['state'].nunique())

df.to_csv("aadhaar_monthly_enrolment_all_states.csv", index=False)

print("\nFile saved as aadhaar_monthly_enrolment_all_states.csv")
