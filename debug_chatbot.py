import google.generativeai as genai

# Test the API connection and basic functionality
def test_api():
    try:
        genai.configure(api_key="AIzaSyAquFtvl1hpeEWB4AzDploXMyygZwIWqWI")
        model = genai.GenerativeModel('gemini-2.5-flash')
        
        print("🔍 Testing API connection...")
        response = model.generate_content("Hello, can you respond with 'API working'?")
        print(f"✅ API Response: {response.text}")
        
        print("\n🔍 Testing symptom extraction...")
        test_message = "I have fever and headache"
        prompt = f"""
        Extract symptoms from this message: "{test_message}"
        Return only a Python list of symptoms in lowercase.
        Example: ["fever", "headache"]
        """
        response = model.generate_content(prompt)
        print(f"📋 Symptom extraction result: {response.text}")
        
        print("\n🔍 Testing treatment generation...")
        symptoms = ["fever", "headache"]
        prompt = f"""
        Provide Ayurvedic treatment for: {', '.join(symptoms)}
        
        Format:
        🌿 **Ayurvedic Medicine**: [medicine name]
        📋 **Dosage**: [how to take]
        """
        response = model.generate_content(prompt)
        print(f"🌿 Treatment result: {response.text}")
        
    except Exception as e:
        print(f"❌ Error: {e}")

if __name__ == "__main__":
    test_api()
