import requests
import json

def test_homeopathy_symptoms():
    """Test homeopathy specific symptoms and search"""
    
    print("=== Testing Homeopathy Symptoms ===\n")
    
    # Get all symptoms from API
    try:
        response = requests.get("http://localhost:8000/get_all_symptoms")
        if response.status_code == 200:
            data = response.json()
            all_symptoms = data['symptoms']
            print(f"Total symptoms available: {len(all_symptoms)}")
            
            # Filter homeopathy-specific symptoms
            homeo_specific = [s for s in all_symptoms if any(keyword in s.lower() for keyword in 
                            ['dry lips', 'cracking', 'white patches', 'oral', 'mouth', 'salivary', 'gums', 'tongue'])]
            
            print(f"Homeopathy-specific symptoms found: {len(homeo_specific)}")
            print("Sample homeopathy symptoms:")
            for i, symptom in enumerate(homeo_specific[:15], 1):
                print(f"{i:2d}. {symptom}")
                
        else:
            print(f"API Error: {response.status_code}")
            return
    except Exception as e:
        print(f"API Error: {e}")
        return
    
    # Test specific homeopathy symptom searches
    print(f"\n=== Testing Homeopathy Searches ===")
    
    test_cases = [
        {
            "name": "Dry Lips + Cracking",
            "symptoms": "dry lips,cracking",
            "treatment": "homeopathy"
        },
        {
            "name": "White Patches + Mouth",
            "symptoms": "white patches in mouth,irritation", 
            "treatment": "homeopathy"
        },
        {
            "name": "Painful Ulcers + Burning",
            "symptoms": "painful ulcers,burning sensation",
            "treatment": "homeopathy"
        },
        {
            "name": "Swollen Gums + Pain",
            "symptoms": "swollen gums,pain",
            "treatment": "homeopathy"
        }
    ]
    
    for test_case in test_cases:
        print(f"\n--- {test_case['name']} ---")
        print(f"Symptoms: {test_case['symptoms']}")
        
        try:
            params = {
                "symptoms": test_case['symptoms'],
                "treatment_type": test_case['treatment'],
                "lang": "en"
            }
            response = requests.get("http://localhost:8000/search_by_symptoms", params=params)
            
            if response.status_code == 200:
                data = response.json()
                if 'results' in data and data['results']:
                    print(f"Found {len(data['results'])} results:")
                    for i, result in enumerate(data['results'][:3], 1):
                        print(f"  {i}. {result['disease']} - {result['medicine']}")
                        print(f"     Matched: {', '.join(result['matched_symptoms'])}")
                elif 'error' in data:
                    print(f"Error: {data['error']}")
                else:
                    print("No results found")
            else:
                print(f"HTTP Error: {response.status_code}")
                
        except Exception as e:
            print(f"Search Error: {e}")

if __name__ == "__main__":
    test_homeopathy_symptoms()
