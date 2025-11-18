import requests
import json

def test_migraine_search():
    """Test migraine symptom search in Ayurveda"""
    url = "http://localhost:8000/search_by_symptoms"
    
    # Test cases for migraine
    test_cases = [
        {
            "name": "Direct Migraine Search",
            "params": {"symptoms": "migraine", "treatment_type": "ayurveda", "lang": "en"}
        },
        {
            "name": "Migraine with Headache",
            "params": {"symptoms": "migraine,headache", "treatment_type": "ayurveda", "lang": "en"}
        },
        {
            "name": "Headache Search",
            "params": {"symptoms": "headache", "treatment_type": "ayurveda", "lang": "en"}
        },
        {
            "name": "Sensitivity to Light",
            "params": {"symptoms": "sensitivity to light", "treatment_type": "ayurveda", "lang": "en"}
        },
        {
            "name": "All Treatment Types for Migraine",
            "params": {"symptoms": "migraine,headache", "treatment_type": "all", "lang": "en"}
        }
    ]
    
    for test_case in test_cases:
        print(f"\n{'='*60}")
        print(f"TEST: {test_case['name']}")
        print(f"Symptoms: {test_case['params']['symptoms']}")
        print(f"{'='*60}")
        
        try:
            response = requests.get(url, params=test_case['params'])
            print(f"Status Code: {response.status_code}")
            
            if response.status_code == 200:
                data = response.json()
                if 'results' in data and data['results']:
                    print(f"Found {len(data['results'])} results:")
                    
                    for i, result in enumerate(data['results'], 1):
                        print(f"\n{i}. Disease: {result['disease']}")
                        print(f"   Type: {result['type']}")
                        print(f"   Medicine: {result['medicine']}")
                        print(f"   Matched Symptoms: {', '.join(result['matched_symptoms'])}")
                        print(f"   Match Count: {result['match_count']}/{result['total_symptoms_searched']}")
                        if 'dosage' in result:
                            print(f"   Dosage: {result['dosage']}")
                elif 'error' in data:
                    print(f"Error: {data['error']}")
                else:
                    print("No results found")
            else:
                print(f"HTTP Error: {response.status_code}")
                
        except Exception as e:
            print(f"Error: {e}")

if __name__ == "__main__":
    test_migraine_search()
