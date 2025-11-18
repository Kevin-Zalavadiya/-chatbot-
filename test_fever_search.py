import requests
import json

# Test the fever search
url = "http://localhost:8000/search_by_symptoms"
params = {
    "symptoms": "fever,headache",
    "treatment_type": "all",
    "lang": "en"
}

try:
    response = requests.get(url, params=params)
    print(f"Status Code: {response.status_code}")
    print(f"Response: {json.dumps(response.json(), indent=2)}")
except Exception as e:
    print(f"Error: {e}")

# Test with just fever
params2 = {
    "symptoms": "fever,body ache",
    "treatment_type": "all", 
    "lang": "en"
}

try:
    response2 = requests.get(url, params=params2)
    print(f"\n--- Fever + Body Ache ---")
    print(f"Status Code: {response2.status_code}")
    print(f"Response: {json.dumps(response2.json(), indent=2)}")
except Exception as e:
    print(f"Error: {e}")
