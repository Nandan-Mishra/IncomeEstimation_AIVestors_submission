import pandas as pd
import joblib
from sklearn.impute import SimpleImputer
from sklearn.preprocessing import LabelEncoder
import os

# Load trained model
model = joblib.load("output/income_model.pkl")

# Load test data
df = pd.read_csv("data/Hackathon_bureau_data_400.csv")
ids = df["id"]
# Preprocess like training
df.drop(["id", "pin", "target_income"], axis=1, inplace=True)

cat_cols = df.select_dtypes(include="object").columns
num_cols = df.select_dtypes(include=["int64", "float64"]).columns

df[num_cols] = SimpleImputer(strategy="median").fit_transform(df[num_cols])
for col in cat_cols:
    df[col] = df[col].fillna("missing")
    df[col] = LabelEncoder().fit_transform(df[col])

# Predict
predictions = model.predict(df)

# Output CSV
output_df = pd.DataFrame({"id": ids, "predicted_income": predictions})
output_df.to_csv("output/output_Hackathon_bureau_data_400.csv", index=False)
print("Inference done. Results saved in output/")

print(predictions)