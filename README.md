# Aadhaar Enrolment Pattern Analysis using UIDAI Data

This repository contains a data‑driven analysis of Aadhaar enrolment patterns in India using official UIDAI enrolment data. The project focuses on identifying temporal trends, regional disparities, and demographic patterns to derive insights that can support evidence‑based administrative and operational decision‑making.

---

## 📌 Project Overview

Aadhaar is a foundational digital identity system in India, supporting access to public services and welfare schemes. Given the large scale of enrolment activity across states and age groups, systematic analysis of enrolment data is essential to understand enrolment behaviour and improve planning.

This project performs exploratory data analysis (EDA) on UIDAI Aadhaar enrolment data to answer key questions such as:
- How does Aadhaar enrolment vary over time?
- How is enrolment distributed across states?
- Which age groups contribute most to enrolment?
- Are there periods of unusually high or low enrolment?

---

## 📂 Dataset

- **Source:** UIDAI Aadhaar Enrolment Dataset  
- **Platform:** data.gov.in  
- **Type:** Administrative enrolment records  

### Key Columns Used
- `date` – Date of enrolment  
- `state` – State / Union Territory  
- `district` – District name  
- `pincode` – Geographic pincode  
- `age_0_5` – Enrolments for ages 0–5  
- `age_5_17` – Enrolments for ages 5–17  
- `age_18_greater` – Enrolments for ages 18+  

### Derived Columns
- `total_enrolment` – Sum of all age‑group enrolments  
- `year` – Extracted from date  
- `month` – Extracted from date  

---

## 🛠️ Tools & Technologies

- Python  
- Pandas  
- Matplotlib  
- VS Code  

---

## 🧹 Data Cleaning & Preprocessing

The raw dataset was cleaned and prepared using the following steps:
- Standardisation of date formats and removal of invalid dates  
- Conversion of enrolment columns to numeric data types  
- Creation of derived features such as total enrolment, year, and month  
- Consistency checks for state and district names  
- Final validation to ensure data completeness and correctness  

The cleaned dataset was saved as `aadhaar_cleaned.csv` and used for all subsequent analysis.

---

## 📊 Analysis Performed

### 1. Time‑Based Analysis
- Monthly Aadhaar enrolment trends
- Yearly enrolment comparison
- Identification of peak and low enrolment periods

### 2. State‑Wise Analysis
- Ranking of states by total enrolment
- Analysis of top, middle, and bottom enrolment states
- Identification of regional disparities

### 3. Age‑Group Analysis
- Comparison of enrolments across age groups (0–5, 5–17, 18+)
- Identification of dominant demographic groups

### 4. Anomaly Observation
- Detection of unusually high or low enrolment periods using statistical comparison

├── data/
│ ├── aadhaar_raw.csv
│ └── aadhaar_cleaned.csv
│
├── scripts/
│ ├── clean_aadhaar_data.py
│ ├── time_based_analysis.py
│ ├── state_wise_analysis.py
│ ├── age_group_analysis.py
│ └── insights_anomalies.py
│
├── visualizations/
│ └── charts_and_plots/
│
├── report/
│ └── Aadhaar_Enrolment_Analysis_Report.pdf
│
└── README.md
---

## 📈 Key Insights

- Aadhaar enrolment shows significant variation across months.
- A small number of states contribute a large share of total enrolments.
- Most states fall into a moderate enrolment range.
- Adult enrolments (18+) dominate overall registrations.
- Temporal anomalies suggest the influence of enrolment drives and operational factors.

---

## ✅ Conclusions

The analysis demonstrates that Aadhaar enrolment patterns are influenced by time, geography, and demographics. Regional disparities and age‑group dominance highlight the importance of targeted enrolment strategies and continuous data‑driven monitoring.

---

## 🔮 Future Scope

- Time‑series forecasting of enrolment demand  
- District‑ and pincode‑level analysis  
- Integration with socio‑economic indicators  
- Automated anomaly detection  
- Development of real‑time dashboards  

---

## 👥 Team

**Team Name:** DataSynth  
**Members:**  
- Bhuvan M S  
- Purvi S Kiran  

**Institution:** Nitte Meenakshi Institute of Technology  

---

## 📄 License

This project is developed for academic and hackathon purposes using publicly available UIDAI data.

---

## 📁 Repository Structure
