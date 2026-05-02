# Financial Fraud Detection System


A machine learning project that analyzes large-scale financial transaction data to detect fraudulent activity using SQL, Python, and ML models.

---

## Project Overview

Financial fraud causes billions in losses every year. This project builds an end-to-end fraud detection pipeline that:
- Analyzes transaction data using SQL to find anomalies
- Trains machine learning models to classify fraud vs legitimate transactions
- Automatically generates summary reports of fraud patterns

---

## Features

- SQL-based anomaly detection (high-risk amounts, late night transactions, suspicious countries)
- Random Forest Classifier — **92% accuracy**
- Logistic Regression baseline model
- Automated fraud report generation (CSV + text summary)

---

## Tech Stack

| Tool | Purpose |
|------|---------|
| Python 3 | Core programming language |
| Pandas | Data manipulation |
| Scikit-learn | Machine learning models |
| SQLite | SQL-based analysis |
| Matplotlib | Data visualization |
| Git & GitHub | Version control |

---

## Project Structure

fraud_detection/
- data - transactions.csv       # Generated transaction dataset (1000 rows)
  src/
   - generate_data.py       # Creates synthetic transaction data
   - sql_analysis.py        # SQL queries to find anomalies
   - train_model.py         # Trains Random Forest + Logistic Regression
   - report_generator.py   # Auto-generates fraud summary reports
- reports/
   - fraud_summary.csv      # Key fraud metrics
   - fraud_report.txt       # Full text report
   - rf_model.pkl           # Saved trained model
- requirements.txt
- README.md


---

## How to Run

**1. Clone the repository**
```bash
git clone https://github.com/YOUR_USERNAME/fraud-detection.git
cd fraud-detection
```

**2. Install dependencies**
```bash
pip install -r requirements.txt
```

**3. Run scripts in order**
```bash
python3 src/generate_data.py       # Create dataset
python3 src/sql_analysis.py        # Run SQL analysis
python3 src/train_model.py         # Train ML models
python3 src/report_generator.py    # Generate reports
```

---

## Results

- Total transactions analyzed — **1000**
- Fraud cases detected — **~85**
- Random Forest accuracy — **92%**
- Logistic Regression accuracy — **~85%**

---

## Key Findings from SQL Analysis

- Transactions above **₹800** had significantly higher fraud rates
- Countries like **NG and RU** showed the highest fraud percentages
- **Late night transactions (12am–5am)** were 3x more likely to be fraudulent
- Customers using a **new device** had double the fraud rate

---
