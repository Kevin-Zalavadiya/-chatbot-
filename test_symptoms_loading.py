import requests
import pandas as pd

def test_symptoms_loading():
    """Test if all symptoms are being loaded properly from all datasets"""
    
    print("=== Testing Symptoms Loading ===\n")
    
    # Test API endpoint
    try:
        response = requests.get("http://localhost:8000/get_all_symptoms")
        if response.status_code == 200:
            api_data = response.json()
            api_symptoms = set(api_data['symptoms'])
            print(f"API returned {len(api_symptoms)} total symptoms")
        else:
            print(f"API Error: {response.status_code}")
            return
    except Exception as e:
        print(f"API Error: {e}")
        return
    
    # Load datasets directly and count symptoms
    print("\n=== Direct Dataset Analysis ===")
    
    # Homeopathy dataset
    try:
        homeo_df = pd.read_csv("d:/chatbot/health-chatbot-backend/sample_20_diseases_detailed_symptoms_homeopathy_sources.csv")
        homeo_symptoms = set()
        for _, row in homeo_df.iterrows():
            symptoms = [s.strip() for s in str(row["Symptoms"]).split(",") if s.strip()]
            homeo_symptoms.update(symptoms)
        print(f"Homeopathy dataset: {len(homeo_symptoms)} unique symptoms")
        print(f"Sample homeopathy symptoms: {list(homeo_symptoms)[:10]}")
    except Exception as e:
        print(f"Homeopathy loading error: {e}")
    
    # Home remedies dataset  
    try:
        home_df = pd.read_csv("d:/chatbot/health-chatbot-backend/home_remedies.csv")
        home_symptoms = set()
        for _, row in home_df.iterrows():
            symptoms = [s.strip() for s in str(row["Symptoms"]).split(",") if s.strip()]
            home_symptoms.update(symptoms)
        print(f"Home remedies dataset: {len(home_symptoms)} unique symptoms")
        print(f"Sample home remedy symptoms: {list(home_symptoms)[:10]}")
    except Exception as e:
        print(f"Home remedies loading error: {e}")
    
    # Ayurveda dataset
    try:
        ayur_df = pd.read_csv("d:/chatbot/health-chatbot-backend/ayurveda_treatments.csv")
        ayur_symptoms = set()
        for _, row in ayur_df.iterrows():
            symptoms = [s.strip() for s in str(row["Symptoms"]).split(",") if s.strip()]
            ayur_symptoms.update(symptoms)
        print(f"Ayurveda dataset: {len(ayur_symptoms)} unique symptoms")
        print(f"Sample ayurveda symptoms: {list(ayur_symptoms)[:10]}")
    except Exception as e:
        print(f"Ayurveda loading error: {e}")
    
    # Check if specific symptoms are in API response
    print(f"\n=== Checking Specific Symptoms ===")
    test_symptoms = [
        "dry lips", "cracking", "white patches in mouth", "painful ulcers", 
        "burning sensation", "swollen gums", "fever", "headache", "migraine"
    ]
    
    for symptom in test_symptoms:
        if symptom.lower() in [s.lower() for s in api_symptoms]:
            print(f"[YES] '{symptom}' found in API")
        else:
            print(f"[NO] '{symptom}' NOT found in API")

if __name__ == "__main__":
    test_symptoms_loading()
