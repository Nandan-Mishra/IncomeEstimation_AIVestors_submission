import os
import pandas as pd
import numpy as np
import time
from sklearn.model_selection import train_test_split, RandomizedSearchCV
from sklearn.ensemble import RandomForestRegressor
from sklearn.metrics import mean_absolute_error, mean_squared_error, r2_score
from sklearn.impute import SimpleImputer
from sklearn.preprocessing import LabelEncoder
import joblib

# Create required folders
os.makedirs("data", exist_ok=True)
os.makedirs("output", exist_ok=True)

# Load the dataset
df = pd.read_csv("data/Hackathon_bureau_data_400.csv")

# Drop unnecessary columns
df.drop(["id", "pin"], axis=1, inplace=True)

# Feature engineering (if both columns exist)
if "age" in df.columns and "experience" in df.columns:
    df["age_minus_experience"] = df["age"] - df["experience"]

# Separate target and features
y = df["target_income"]
X = df.drop("target_income", axis=1)

# Identify numerical and categorical columns
cat_cols = X.select_dtypes(include="object").columns
num_cols = X.select_dtypes(include=["float64", "int64"]).columns

# Handle missing values
X[num_cols] = SimpleImputer(strategy="median").fit_transform(X[num_cols])

# Encode categorical columns using LabelEncoder
label_encoders = {}
for col in cat_cols:
    X[col] = X[col].fillna("missing")
    le = LabelEncoder()
    X[col] = le.fit_transform(X[col])
    label_encoders[col] = le

# Save label encoders for inference
joblib.dump(label_encoders, "output/label_encoders.pkl")

# Train/test split
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)

# Define hyperparameter search space
param_dist = {
    "n_estimators": [300, 400, 500, 600],
    "max_depth": [20, 30, 40, None],
    "min_samples_split": [2, 5, 10],
    "min_samples_leaf": [1, 2, 4],
    "max_features": ["auto", "sqrt", "log2"]
}

# Random Forest + Hyperparameter tuning
random_search = RandomizedSearchCV(
    RandomForestRegressor(random_state=42),
    param_distributions=param_dist,
    n_iter=50,
    cv=3,
    scoring="neg_mean_absolute_error",
    n_jobs=-1,
    verbose=1,
    random_state=42
)

# Train model
random_search.fit(X_train, y_train)
best_model = random_search.best_estimator_

# Predict on test set
y_pred = best_model.predict(X_test)

# Evaluate
mae = mean_absolute_error(y_test, y_pred)
rmse = mean_squared_error(y_test, y_pred, squared=False)
r2 = r2_score(y_test, y_pred)

# Population coverage metrics
percentage_deviation = np.abs(y_test - y_pred) / y_test
coverage_25pct = np.mean(percentage_deviation <= 0.25) * 100

abs_diff = np.abs(y_test - y_pred)
coverage_5k = np.mean(abs_diff <= 5000) * 100

# Print evaluation results
print("\n✅ Best Parameters:", random_search.best_params_)
print("📉 MAE:", mae)
print("📈 RMSE:", rmse)
print("📊 R² Score:", r2)
print("📈 Coverage within 25% deviation: {:.2f}%".format(coverage_25pct))
print("💰 Coverage within ₹5,000 error: {:.2f}%".format(coverage_5k))