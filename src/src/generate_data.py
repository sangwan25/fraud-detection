import pandas as pd
import numpy as np
import random

random.seed(42)
np.random.seed(42)

n = 1000

data = {
    "transaction_id": range(1, n + 1),
    "customer_id": np.random.randint(1000, 1200, n),
    "amount": np.round(np.random.exponential(scale=200, size=n), 2),
    "merchant_category": np.random.choice(["grocery", "electronics", "travel", "gas", "online"], n),
    "transaction_hour": np.random.randint(0, 24, n),
    "country": np.random.choice(["IN", "US", "UK", "NG", "RU"], n, p=[0.6, 0.2, 0.1, 0.05, 0.05]),
    "num_transactions_today": np.random.randint(1, 20, n),
    "account_age_days": np.random.randint(10, 3000, n),
    "is_new_device": np.random.choice([0, 1], n, p=[0.8, 0.2]),
}

df = pd.DataFrame(data)

fraud_score = (
    (df["amount"] > 800).astype(int) * 3 +
    (df["transaction_hour"] < 5).astype(int) * 2 +
    (df["is_new_device"] == 1).astype(int) * 2 +
    (df["country"].isin(["NG", "RU"])).astype(int) * 3 +
    (df["num_transactions_today"] > 15).astype(int) * 2
)
df["is_fraud"] = (fraud_score >= 5).astype(int)

df.to_csv("data/transactions.csv", index=False)
print(f"Dataset created: {len(df)} rows, {df['is_fraud'].sum()} fraud cases")