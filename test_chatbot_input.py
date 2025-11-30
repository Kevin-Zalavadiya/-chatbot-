from health_chatbot import HealthChatbot

def test_chatbot():
    print("🧪 Testing Health Chatbot")
    print("=" * 40)
    
    bot = HealthChatbot("AIzaSyAquFtvl1hpeEWB4AzDploXMyygZwIWqWI")
    
    test_cases = [
        "I have fever and headache",
        "ayurvedic treatment for cold",
        "home remedies for stomach pain",
        "homeopathy for anxiety"
    ]
    
    for i, test in enumerate(test_cases, 1):
        print(f"\n📝 Test {i}: {test}")
        print("-" * 30)
        try:
            response = bot.chat(test)
            print(f"🤖 Response: {response[:200]}...")
        except Exception as e:
            print(f"❌ Error: {e}")
        print()

if __name__ == "__main__":
    test_chatbot()
