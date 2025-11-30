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
        """
        response = self.model.generate_content(prompt)
        try:
            return eval(response.text.strip())
        except:
            return ["not_enough_symptoms"]
    
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
        if treatment_type == "ayurveda":
            prompt = f"""
            Provide ONLY Ayurvedic treatment for symptoms: {symptoms}
            
            Format:
            🌿 **Ayurvedic Medicine**: [medicine name]
            📋 **Dosage**: [how to take]
            ⚠️ **Precautions**: [what to avoid]
            🏠 **Home Tips**: [additional advice]
            
            Keep response focused only on Ayurvedic treatments.
            """
        
        elif treatment_type == "homeopathy":
            prompt = f"""
            Provide ONLY Homeopathic treatment for symptoms: {symptoms}
            
            Format:
            🌸 **Homeopathic Medicine**: [medicine name]
            📋 **Dosage**: [how to take]
            ⚠️ **Precautions**: [what to avoid]
            🏠 **Home Tips**: [additional advice]
            
            Keep response focused only on Homeopathic treatments.
            """
        
        elif treatment_type == "home remedy":
            prompt = f"""
            Provide ONLY Home Remedies for symptoms: {symptoms}
            
            Format:
            🏠 **Home Remedy**: [remedy name]
            📋 **How to Use**: [instructions]
            ⚠️ **Precautions**: [warnings]
            🌿 **Benefits**: [why it helps]
            
            Keep response focused only on natural home remedies.
            """
        
        else:  # all types
            prompt = f"""
            Provide treatments for symptoms: {symptoms}
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
        
        if symptoms == ["not_enough_symptoms"]:
            return "Please mention at least two symptoms for better recommendations."
        
        return self.get_treatment(symptoms, treatment_type)

# Demo Test
def demo():
    print("🏥 Health Chatbot Demo")
    print("=" * 50)
    
    bot = HealthChatbot("AIzaSyAquFtvl1hpeEWB4AzDploXMyygZwIWqWI")
    
    test_messages = [
        "ayurvedic treatment for fever and headache",
        "homeopathy for cold and cough",
        "home remedies for stomach pain",
        "I have fever since morning and my head is hurting badly"
    ]
    
    for i, message in enumerate(test_messages, 1):
        print(f"\n📝 Test {i}: {message}")
        print("-" * 40)
        try:
            response = bot.chat(message)
            print(response)
        except Exception as e:
            print(f"❌ Error: {e}")
        print("\n" + "=" * 50)

if __name__ == "__main__":
    demo()
