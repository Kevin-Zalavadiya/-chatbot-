import requests
import json

def test_fever_search():
    """Test the improved fever search functionality"""
    url = "http://localhost:8000/search_by_symptoms"
    
    # Test cases for fever
    test_cases = [
        {
            "name": "Basic Fever Search",
            "params": {"symptoms": "fever,headache", "treatment_type": "all", "lang": "en"}
        },
        {
            "name": "Fever with Body Ache",
            "params": {"symptoms": "fever,body ache", "treatment_type": "all", "lang": "en"}
        },
        {
            "name": "High Fever Search",
            "params": {"symptoms": "high temperature,chills", "treatment_type": "all", "lang": "en"}
        },
        {
            "name": "Home Remedies Only",
            "params": {"symptoms": "fever,weakness", "treatment_type": "home_remedy", "lang": "en"}
        },
        {
            "name": "Homeopathy Only",
            "params": {"symptoms": "fever,fatigue", "treatment_type": "homeopathy", "lang": "en"}
        }
    ]
    
    for test_case in test_cases:
        print(f"\n{'='*50}")
        print(f"TEST: {test_case['name']}")
        print(f"{'='*50}")
        
        try:
            response = requests.get(url, params=test_case['params'])
            print(f"Status Code: {response.status_code}")
            
            if response.status_code == 200:
                data = response.json()
                if 'results' in data:
                    print(f"Found {len(data['results'])} results:")
                    for i, result in enumerate(data['results'][:3], 1):  # Show first 3 results
                        print(f"\n{i}. Disease: {result['disease']}")
                        print(f"   Type: {result['type']}")
                        print(f"   Medicine: {result['medicine']}")
                        print(f"   Matched Symptoms: {', '.join(result['matched_symptoms'])}")
                        if 'dosage' in result:
                            print(f"   Dosage: {result['dosage']}")
                else:
                    print(f"Error: {data.get('error', 'Unknown error')}")
            else:
                print(f"HTTP Error: {response.status_code}")
                
        except Exception as e:
            print(f"Error: {e}")

if __name__ == "__main__":
    test_fever_search()
