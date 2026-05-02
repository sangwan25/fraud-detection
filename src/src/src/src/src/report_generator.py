import pandas as pd
import sqlite3
from datetime import datetime

df = pd.read_csv("data/transactions.csv")
conn = sqlite3.connect(":memory:")
df.to_sql("transactions", conn, index=False)

total = len(df)
total_fraud = int(df["is_fraud"].sum())
fraud_rate = round(100 * total_fraud / total, 2)
avg_fraud_amount = round(df[df["is_fraud"] == 1]["amount"].mean(), 2)

fraud_by_country = pd.read_sql("""
    SELECT country, SUM(is_fraud) as frauds
    FROM transactions GROUP BY country ORDER BY frauds DESC
""", conn)

summary = pd.DataFrame({
    "metric": ["Total Transactions", "Total Fraud Cases", "Fraud Rate (%)", "Avg Fraud Amount"],
    "value": [total, total_fraud, fraud_rate, avg_fraud_amount]
})
summary.to_csv("reports/fraud_summary.csv", index=False)

report_text = f"""
FRAUD DETECTION REPORT
Generated: {datetime.now().strftime('%Y-%m-%d %H:%M')}
{'='*40}
Total Transactions Analyzed : {total}
Total Fraud Cases Detected  : {total_fraud}
Fraud Rate                  : {fraud_rate}%
Average Fraud Amount        : {avg_fraud_amount}

Top Countries by Fraud:
{fraud_by_country.to_string(index=False)}
"""

with open("reports/fraud_report.txt", "w") as f:
    f.write(report_text)

print(report_text)
print("Reports saved in /reports folder")
conn.close()