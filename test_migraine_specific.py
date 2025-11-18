import requests
import json

def test_migraine_specific():
    """Test migraine with more specific symptoms"""
    url = "http://localhost:8000/search_by_symptoms"
    
    # Test cases with migraine-specific symptoms
    test_cases = [
        {
            "name": "Migraine with Nausea",
            "params": {"symptoms": "severe headache,nausea", "treatment_type": "ayurveda", "lang": "en"}
        },
        {
            "name": "Migraine with Light Sensitivity", 
            "params": {"symptoms": "severe headache,sensitivity to light", "treatment_type": "ayurveda", "lang": "en"}
        },
        {
            "name": "Throbbing Pain with Vomiting",
            "params": {"symptoms": "throbbing pain,vomiting", "treatment_type": "ayurveda", "lang": "en"}
        },
        {
            "name": "Visual Disturbances with Headache",
            "params": {"symptoms": "visual disturbances,severe headache", "treatment_type": "ayurveda", "lang": "en"}
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
    test_migraine_specific()
