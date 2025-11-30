import requests
import json

def test_backend():
    base_url = "http://localhost:8000"
    
    print("🧪 Testing New Chatbot Backend")
    print("=" * 40)
    
    # Test 1: Root endpoint
    try:
        response = requests.get(f"{base_url}/")
        print(f"✅ Root: {response.json()}")
    except Exception as e:
        print(f"❌ Root error: {e}")
        return
    
    # Test 2: Chat endpoint
    test_cases = [
        {"symptoms": "fever, headache", "treatment_type": "all"},
        {"symptoms": "cold, cough", "treatment_type": "ayurveda"},
        {"symptoms": "stomach pain", "treatment_type": "home_remedy"}
    ]
    
    for i, test in enumerate(test_cases, 1):
        print(f"\n📝 Test {i}: {test}")
        try:
            response = requests.post(
                f"{base_url}/chat",
                json=test,
                timeout=30
            )
            if response.status_code == 200:
                result = response.json()
                print(f"✅ Success: {result['response'][:200]}...")
            else:
                print(f"❌ Status {response.status_code}: {response.text}")
        except Exception as e:
            print(f"❌ Error: {e}")

if __name__ == "__main__":
    test_backend()
