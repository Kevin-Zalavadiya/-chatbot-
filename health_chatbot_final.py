import google.generativeai as genai

class HealthChatbot:
    def __init__(self, api_key):
        genai.configure(api_key=api_key)
        self.model = genai.GenerativeModel('gemini-2.5-flash')
    
    def extract_symptoms(self, text):
        prompt = f"""
        Extract symptoms from this message: "{text}"
        Return only a Python list of symptoms in lowercase.
        Example: ["fever", "headache"]
        
        Rules:
        - Extract ALL symptoms mentioned
        - Convert variations: "head hurting" → "headache", "feverish" → "fever"
        - If only 1 symptom found, still return it
        - If no symptoms, return []
        """
        response = self.model.generate_content(prompt)
        try:
            symptoms = eval(response.text.strip())
            return symptoms if symptoms and symptoms != [] else ["general_discomfort"]
        except:
            return ["general_discomfort"]
    
    def detect_treatment_type(self, message):
        message = message.lower()
        if "ayurved" in message:
            return "ayurveda"
        elif "homeopath" in message:
            return "homeopathy" 
        elif "home remedy" in message or "home remedies" in message:
            return "home remedy"
        else:
            return "all"
    
    def get_treatment(self, symptoms, treatment_type):
        symptoms_str = ", ".join(symptoms)
        
        if treatment_type == "ayurveda":
            prompt = f"""
            Provide ONLY Ayurvedic treatment for: {symptoms_str}
            
            Format:
            🌿 **Ayurvedic Medicine**: [medicine name]
            📋 **Dosage**: [how to take]
            ⚠️ **Precautions**: [what to avoid]
            🏠 **Home Tips**: [additional advice]
            
            Keep response focused only on Ayurvedic treatments.
            """
        
        elif treatment_type == "homeopathy":
            prompt = f"""
            Provide ONLY Homeopathic treatment for: {symptoms_str}
            
            Format:
            🌸 **Homeopathic Medicine**: [medicine name]
            📋 **Dosage**: [how to take]
            ⚠️ **Precautions**: [what to avoid]
            🏠 **Home Tips**: [additional advice]
            
            Keep response focused only on Homeopathic treatments.
            """
        
        elif treatment_type == "home remedy":
            prompt = f"""
            Provide ONLY Home Remedies for: {symptoms_str}
            
            Format:
            🏠 **Home Remedy**: [remedy name]
            📋 **How to Use**: [instructions]
            ⚠️ **Precautions**: [warnings]
            🌿 **Benefits**: [why it helps]
            
            Keep response focused only on natural home remedies.
            """
        
        else:  # all types
            prompt = f"""
            Provide treatments for: {symptoms_str}
            Include all three types: Ayurvedic, Homeopathy, and Home Remedies.
            
            Format:
            🌿 **Ayurvedic**: [medicine] - [dosage]
            🌸 **Homeopathy**: [medicine] - [dosage]  
            🏠 **Home Remedy**: [remedy] - [how to use]
            
            Keep each treatment type separate and clear.
            """
        
        response = self.model.generate_content(prompt)
        return response.text
    
    def chat(self, user_message):
        symptoms = self.extract_symptoms(user_message)
        treatment_type = self.detect_treatment_type(user_message)
        
        if symptoms == ["general_discomfort"]:
            return "Please describe your symptoms more specifically for better recommendations."
        
        return self.get_treatment(symptoms, treatment_type)

# Interactive Chatbot
def interactive_chat():
    print("🏥 Ayurvedic Health Chatbot")
    print("=" * 50)
    print("Types: ayurvedic, homeopathy, home remedies")
    print("Type 'quit' to exit")
    print("=" * 50)
    
    bot = HealthChatbot("AIzaSyAquFtvl1hpeEWB4AzDploXMyygZwIWqWI")
    
    while True:
        user_input = input("\n👤 You: ").strip()
        
        if user_input.lower() in ['quit', 'exit', 'bye']:
            print("👋 Take care! Stay healthy!")
            break
        
        if not user_input:
            continue
            
        print("\n🤖 Bot: ", end="")
        try:
            response = bot.chat(user_input)
            print(response)
        except Exception as e:
            print(f"❌ Error: {e}")

# Quick Test
def quick_test():
    print("🧪 Quick Test Mode")
    print("=" * 30)
    
    bot = HealthChatbot("AIzaSyAquFtvl1hpeEWB4AzDploXMyygZwIWqWI")
    
    test_cases = [
        "ayurvedic treatment for fever and headache",
        "homeopathy for cold and cough", 
        "home remedies for stomach pain",
        "I have body pain and feel weak"
    ]
    
    for i, test in enumerate(test_cases, 1):
        print(f"\n📝 Test {i}: {test}")
        print("-" * 40)
        try:
            response = bot.chat(test)
            print(response)
        except Exception as e:
            print(f"❌ Error: {e}")
        print()

if __name__ == "__main__":
    print("Choose mode:")
    print("1. Interactive Chat")
    print("2. Quick Test")
    
    choice = input("Enter choice (1 or 2): ").strip()
    
    if choice == "1":
        interactive_chat()
    elif choice == "2":
        quick_test()
    else:
        print("Invalid choice. Running quick test...")
        quick_test()
