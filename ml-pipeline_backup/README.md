# 1. Folder Setup
Make sure your project folder looks like this:

ml-pipeline/
├── main.py
├── run_inference.py
├── requirements.txt
├── .env
├── README.md
├── config/
│ └── config.json
├── data/
│ └── Hackathon_bureau_data_400.csv
└── output/
└── (income_model.pkl will be saved here after training)

# 2. Install Required Packages
Open terminal in the project folder and run:

requirements = """pandas
numpy
scikit-learn
joblib

"""

```bash 
pip install pandas numpy scikit-learn joblib

pip install -r requirements.txt
```

# 3. Train the Model (Optional if already trained) 

```bash 
python main.py
```
This will save:

output/income_model.pkl (model)

output/label_encoders.pkl (for categorical values)

# 4. Run Inference (Predictions)

```bash
python run_inference.py
```

✅ Outputs predictions in:
output/output_Hackathon_bureau_data_400.csv










