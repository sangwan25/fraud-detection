import sqlite3
import pandas as pd

df = pd.read_csv("data/transactions.csv")
conn = sqlite3.connect(":memory:")
df.to_sql("transactions", conn, index=False)

print("=== HIGH RISK TRANSACTIONS (amount > 800) ===")
print(pd.read_sql("""
    SELECT transaction_id, customer_id, amount, country, is_fraud
    FROM transactions
    WHERE amount > 800
    ORDER BY amount DESC
    LIMIT 10
""", conn))

print("\n=== FRAUD BY COUNTRY ===")
print(pd.read_sql("""
    SELECT country,
           COUNT(*) as total_transactions,
           SUM(is_fraud) as fraud_count,
           ROUND(100.0 * SUM(is_fraud) / COUNT(*), 2) as fraud_rate_pct
    FROM transactions
    GROUP BY country
    ORDER BY fraud_rate_pct DESC
""", conn))

print("\n=== LATE NIGHT TRANSACTIONS (midnight to 5am) ===")
print(pd.read_sql("""
    SELECT transaction_hour, COUNT(*) as count, SUM(is_fraud) as frauds
    FROM transactions
    WHERE transaction_hour BETWEEN 0 AND 5
    GROUP BY transaction_hour
""", conn))

conn.close()