import os
import pandas as pd
from fastapi import FastAPI, Query
from fastapi.middleware.cors import CORSMiddleware
from translate import (
    translate_symptoms_list, 
    HINDI_TO_ENGLISH_SYMPTOMS, 
    ENGLISH_TO_HINDI_SYMPTOMS,
    translate_to_hindi_content,
    translate_disease_name
)

# Get the current folder (where main.py is)
BASE_DIR = os.path.dirname(os.path.abspath(__file__))

# Build correct paths for CSVs
homeopathy_csv = os.path.join(BASE_DIR, "sample_20_diseases_detailed_symptoms_homeopathy_sources.csv")
remedies_csv = os.path.join(BASE_DIR, "home_remedies.csv")
ayurveda_csv = os.path.join(BASE_DIR, "ayurveda_treatments.csv")

# Load datasets
homeopathy_df = pd.read_csv(homeopathy_csv)
home_remedies_df = pd.read_csv(remedies_csv)
ayurveda_df = pd.read_csv(ayurveda_csv)

app = FastAPI()

# Enable CORS so frontend can connect
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],  # for dev, allow all
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

@app.get("/")
def root():
    return {"message": "Chatbot API running successfully!"}

@app.get("/get_diseases")
def get_diseases(type: str):
    if type == "homeopathy":
        diseases = homeopathy_df["Disease Name"].unique().tolist()
    elif type == "ayurveda":
        diseases = ayurveda_df["Disease"].unique().tolist()
    else:
        diseases = home_remedies_df["Disease"].unique().tolist()
    return {"diseases": diseases}

@app.get("/get_symptoms")
def get_symptoms(disease: str, type: str):
    if type == "homeopathy":
        row = homeopathy_df[homeopathy_df["Disease Name"].str.lower() == disease.lower()]
        if row.empty:
            return {"error": "Disease not found"}
        symptoms = row.iloc[0]["Symptoms"].split(",")
    elif type == "ayurveda":
        row = ayurveda_df[ayurveda_df["Disease"].str.lower() == disease.lower()]
        if row.empty:
            return {"error": "Disease not found"}
        symptoms = row.iloc[0]["Symptoms"].split(",")
    else:
        row = home_remedies_df[home_remedies_df["Disease"].str.lower() == disease.lower()]
        if row.empty:
            return {"error": "Disease not found"}
        symptoms = row.iloc[0]["Symptoms"].split(",")
    return {"symptoms": [s.strip() for s in symptoms]}

@app.get("/get_all_symptoms")
def get_all_symptoms():
    """Get all unique symptoms from both datasets with Hindi translations"""
    all_symptoms = set()
    
    # Get symptoms from homeopathy data
    for _, row in homeopathy_df.iterrows():
        symptoms = [s.strip() for s in str(row["Symptoms"]).split(",") if s.strip()]
        all_symptoms.update(symptoms)
    
    # Get symptoms from home remedies data
    for _, row in home_remedies_df.iterrows():
        symptoms = [s.strip() for s in str(row["Symptoms"]).split(",") if s.strip()]
        all_symptoms.update(symptoms)
    
    # Get symptoms from ayurveda data
    for _, row in ayurveda_df.iterrows():
        symptoms = [s.strip() for s in str(row["Symptoms"]).split(",") if s.strip()]
        all_symptoms.update(symptoms)
    
    # Add Hindi translations
    english_symptoms = sorted(list(all_symptoms))
    hindi_symptoms = list(HINDI_TO_ENGLISH_SYMPTOMS.keys())
    
    # Combine English and Hindi symptoms
    all_combined = english_symptoms + hindi_symptoms
    
    return {"symptoms": sorted(set(all_combined))}

@app.get("/search_by_symptoms")
def search_by_symptoms(symptoms: str, treatment_type: str = "all", lang: str = "en"):
    """
    Search for treatments by comma-separated symptoms.
    Returns a results list with fields used by the frontend.
    """
    # Basic validation
    user_symptoms = [s.strip() for s in str(symptoms).split(",") if s.strip()]
    if len(user_symptoms) < 2:
        return {
            "error": "Please enter at least 2 symptoms",
            "hindi_error": "कृपया कम से कम 2 लक्षण दर्ज करें"
        }

    # Translate Hindi symptoms to English for matching
    user_symptoms_english = translate_symptoms_list(user_symptoms)
    
    # Normalize for matching
    user_symptoms_lower = [s.lower() for s in user_symptoms_english]

    results = []

    def score_and_append_from_df(df, type_label, disease_col, symptoms_col, medicine_col, extra_fields=None):
        extra_fields = extra_fields or {}
        for _, row in df.iterrows():
            row_symptoms = [s.strip() for s in str(row.get(symptoms_col, "")).split(",") if s.strip()]
            row_symptoms_lower = [s.lower() for s in row_symptoms]
            if not row_symptoms_lower:
                continue

            # Match English symptoms and map back to original user input
            matched_original = []
            for i, eng_symptom in enumerate(user_symptoms_english):
                if eng_symptom.lower() in row_symptoms_lower:
                    # Use the original user input (Hindi or English)
                    matched_original.append(user_symptoms[i])
            
            match_count = len(matched_original)
            if match_count == 0:
                continue

            total = len(user_symptoms)
            confidence = int(round((match_count / total) * 100))

            item = {
                "disease": str(row.get(disease_col, "Unknown")),
                "type": type_label,
                "matched_symptoms": matched_original,
                "match_count": match_count,
                "total_symptoms_searched": total,
                # Frontend expects medicine or remedy depending on type
                "medicine": str(row.get(medicine_col, "Not specified")),
            }
            # Merge any extra fields
            item.update(extra_fields(row) if callable(extra_fields) else extra_fields)
            results.append((confidence, item))

    # Filter by treatment_type and score
    tt = (treatment_type or "all").lower()

    if tt in ("all", "homeopathy"):
        # Homeopathy dataset
        score_and_append_from_df(
            homeopathy_df,
            "homeopathy",
            disease_col="Disease Name",
            symptoms_col="Symptoms",
            medicine_col="Homeopathy Medicines",
            extra_fields=lambda r: {
                "dosage": str(r.get("Dosage/Usage", "Not specified")) if "Dosage/Usage" in r else "Not specified",
                "precautions": str(r.get("Precautions", "")).strip() if "Precautions" in r else "",
                "possible_causes": str(r.get("Possible Causes", "")).strip() if "Possible Causes" in r else "",
                "home_tips": str(r.get("Home Tips", "")).strip() if "Home Tips" in r else "",
                "source": str(r.get("Source", "Not specified")),
            },
        )

    if tt in ("all", "remedy", "home_remedy", "home remedies", "home_remedies"):
        # Home remedies dataset
        def remedy_extras(r):
            return {
                "home_tips": str(r.get("Home Tips", "")).strip() if "Home Tips" in r else "",
                "precautions": str(r.get("Precautions", "")).strip() if "Precautions" in r else "",
                "possible_causes": str(r.get("Possible Causes", "")).strip() if "Possible Causes" in r else "",
                "dosage": str(r.get("Dosage/Usage", "Not specified")) if "Dosage/Usage" in r else "Not specified",
                "remedy": str(r.get("Home Remedy", r.get("Home Remedies", "Not specified"))),
                "preparation": str(r.get("Preparation", "")).strip() if "Preparation" in r else "",
                "medicine": str(r.get("Home Remedy", r.get("Home Remedies", "Not specified"))),
                "type": "home_remedy",
                "source": str(r.get("Source", "Not specified")),
            }

        score_and_append_from_df(
            home_remedies_df,
            "home_remedy",
            disease_col="Disease",
            symptoms_col="Symptoms",
            medicine_col="Home Remedy",
            extra_fields=remedy_extras,
        )

    if tt in ("all", "ayurveda"):
        # Ayurveda dataset
        def ayurveda_extras(r):
            return {
                "home_tips": str(r.get("Home Tips", "")).strip() if "Home Tips" in r else "",
                "precautions": str(r.get("Precautions", "")).strip() if "Precautions" in r else "",
                "possible_causes": str(r.get("Possible Causes", "")).strip() if "Possible Causes" in r else "",
                "dosage": str(r.get("Dosage/Usage", "Not specified")) if "Dosage/Usage" in r else "Not specified",
                "preparation": str(r.get("Preparation", "")).strip() if "Preparation" in r else "",
                "medicine": str(r.get("Ayurvedic Medicine", "Not specified")),
                "type": "ayurveda",
                "source": str(r.get("Source", "Not specified")),
            }

        score_and_append_from_df(
            ayurveda_df,
            "ayurveda",
            disease_col="Disease",
            symptoms_col="Symptoms",
            medicine_col="Ayurvedic Medicine",
            extra_fields=ayurveda_extras,
        )

    # Sort by confidence desc and cap results
    results.sort(key=lambda x: x[0], reverse=True)
    top = [item for _, item in results[:10]]

    if not top:
        return {
            "error": "No matching treatments found",
            "hindi_error": "कोई मिलान करने वाले उपचार नहीं मिले",
            "suggested_terms": [],
        }

    # Translate content to Hindi if language is Hindi
    if lang == 'hi':
        for item in top:
            # Translate disease name
            item['disease'] = translate_disease_name(item['disease'], lang)
            
            # Translate all text fields
            fields_to_translate = ['medicine', 'remedy', 'dosage', 'preparation', 
                                   'possible_causes', 'home_tips', 'precautions']
            for field in fields_to_translate:
                if field in item and item[field] and item[field] != 'Not specified':
                    item[field] = translate_to_hindi_content(item[field], lang)

    return {"results": top}

@app.get("/get_treatment")
def get_treatment(disease: str, type: str, selected_symptoms: list[str] = Query(...)):
    if len(selected_symptoms) < 2:
        return {"error": "Please select at least 2 symptoms"}

    if type == "homeopathy":
        row = homeopathy_df[homeopathy_df["Disease Name"].str.lower() == disease.lower()]
        if row.empty:
            return {"error": "Disease not found"}
        return {
            "disease": disease,
            "symptoms": selected_symptoms,
            "medicine": row.iloc[0]["Homeopathy Medicines"],
            "source": row.iloc[0]["Source"]
        }
    else:
        row = home_remedies_df[home_remedies_df["Disease"].str.lower() == disease.lower()]
        if row.empty:
            return {"error": "Disease not found"}
        return {
            "disease": disease,
            "symptoms": selected_symptoms,
            "home_remedy": row.iloc[0]["Home Remedy"],
            "preparation": row.iloc[0]["Preparation"],
            "source": row.iloc[0]["Source"]
        }

if __name__ == "__main__":
    import uvicorn
    uvicorn.run(app, host="0.0.0.0", port=8000)