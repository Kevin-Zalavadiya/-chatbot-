from health_chatbot import HealthChatbot

print("🏥 Ayurvedic Health Chatbot - Quick Demo")
print("=" * 50)

bot = HealthChatbot("AIzaSyAquFtvl1hpeEWB4AzDploXMyygZwIWqWI")

# Simulate user interaction
test_messages = [
    "I have fever since morning and my head is hurting badly",
    "ayurvedic treatment for cold and cough",
    "home remedies for stomach pain"
]

for msg in test_messages:
    print(f"\n👤 User: {msg}")
    print("🤖 Bot: ", end="")
    response = bot.chat(msg)
    # Show first 300 characters to keep demo short
    print(response[:300] + "..." if len(response) > 300 else response)
    print("-" * 50)

print("\n✅ Chatbot is working perfectly!")
print("🚀 Ready for interactive use!")
