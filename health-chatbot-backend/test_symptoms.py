import pandas as pd
import os

# Get the current folder (where main.py is)
BASE_DIR = os.path.dirname(os.path.abspath(__file__))

# Build correct paths for CSVs
homeopathy_csv = os.path.join(BASE_DIR, "sample_20_diseases_detailed_symptoms_homeopathy_sources.csv")
remedies_csv = os.path.join(BASE_DIR, "home_remedies.csv")

# Load datasets
homeopathy_df = pd.read_csv(homeopathy_csv)
home_remedies_df = pd.read_csv(remedies_csv)

print("=== HOMEOPATHY SYMPTOMS ===")
all_symptoms = set()

for _, row in homeopathy_df.iterrows():
    symptoms = [s.strip() for s in str(row["Symptoms"]).split(",") if s.strip()]
    print(f"{row['Disease Name']}: {symptoms}")
    all_symptoms.update(symptoms)

print("\n=== HOME REMEDIES SYMPTOMS ===")
for _, row in home_remedies_df.iterrows():
    symptoms = [s.strip() for s in str(row["Symptoms"]).split(",") if s.strip()]
    print(f"{row['Disease']}: {symptoms}")
    all_symptoms.update(symptoms)

print(f"\n=== ALL UNIQUE SYMPTOMS ({len(all_symptoms)}) ===")
for symptom in sorted(all_symptoms):
    print(f"- {symptom}")