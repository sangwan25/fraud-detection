import pandas as pd
from sklearn.model_selection import train_test_split
from sklearn.ensemble import RandomForestClassifier
from sklearn.linear_model import LogisticRegression
from sklearn.metrics import accuracy_score, classification_report
from sklearn.preprocessing import LabelEncoder
import pickle

df = pd.read_csv("data/transactions.csv")

le = LabelEncoder()
df["merchant_category"] = le.fit_transform(df["merchant_category"])
df["country"] = le.fit_transform(df["country"])

features = ["amount", "merchant_category", "transaction_hour", "country",
            "num_transactions_today", "account_age_days", "is_new_device"]
X = df[features]
y = df["is_fraud"]

X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)

rf_model = RandomForestClassifier(n_estimators=100, random_state=42)
rf_model.fit(X_train, y_train)
rf_preds = rf_model.predict(X_test)
print(f"Random Forest Accuracy: {accuracy_score(y_test, rf_preds) * 100:.2f}%")
print(classification_report(y_test, rf_preds))

lr_model = LogisticRegression(max_iter=1000)
lr_model.fit(X_train, y_train)
lr_preds = lr_model.predict(X_test)
print(f"Logistic Regression Accuracy: {accuracy_score(y_test, lr_preds) * 100:.2f}%")

with open("reports/rf_model.pkl", "wb") as f:
    pickle.dump(rf_model, f)
print("Model saved to reports/rf_model.pkl")