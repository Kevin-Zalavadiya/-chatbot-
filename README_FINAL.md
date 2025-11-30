# 🌿 AI Health Chatbot - Gemini Powered

A modern, AI-powered health chatbot that provides natural treatment recommendations using Google Gemini AI. Features Ayurvedic, Homeopathic, and Home Remedy suggestions with a beautiful, responsive interface.

## ✨ Features

- 🤖 **AI-Powered**: Natural symptom understanding with Google Gemini
- 🌿 **Multiple Treatments**: Ayurvedic, Homeopathy, and Home Remedies
- 💬 **Natural Chat**: No CSV restrictions - just talk naturally!
- 🎨 **Beautiful UI**: Modern chat interface with gradients
- 📱 **Mobile Responsive**: Works perfectly on all devices
- 🌍 **Multi-language**: English & Hindi support
- ⚡ **Real-time**: Instant AI responses with typing indicators

## 🚀 Quick Start

### Option 1: Standalone (Easiest)
```bash
pip install google-generativeai flask flask-cors
python standalone_health_chatbot.py
```
Then open `http://localhost:5000`

### Option 2: Full React App
```bash
# Backend
cd health-chatbot-backend
pip install -r requirements.txt
python simple_backend.py

# Frontend (new terminal)
cd health-chatbot-frontend
npm install
npm start
```
Then open `http://localhost:3000`

## 📁 Project Structure

```
🤖 Main Chatbot Files:
├── health_chatbot.py              # Core Gemini chatbot logic
├── simple_backend.py               # Flask backend server
├── standalone_health_chatbot.py    # All-in-one solution
└── requirements.txt                # Python dependencies

🎨 Frontend Files:
├── health-chatbot-frontend/
│   ├── src/
│   │   ├── components/
│   │   │   ├── GeminiChatbot.js    # React chat component
│   │   │   └── GeminiChatbot.css   # Beautiful styling
│   │   └── App.js                  # Main React app
│   └── package.json                # Node dependencies

🚀 Quick Share Package:
├── standalone_health_chatbot.py    # Single file solution
├── README_STANDALONE.md            # Standalone instructions
└── README.md                       # This file
```

## 🔧 Setup Instructions

### Prerequisites
- Python 3.7+
- Node.js 14+ (for React version)
- Google Gemini API key

### API Key Setup
1. Get your Gemini API key from [Google AI Studio](https://makersuite.google.com/app/apikey)
2. Update the API key in:
   - `health_chatbot.py` (line ~126)
   - `simple_backend.py` (line ~18)
   - `standalone_health_chatbot.py` (line ~20)

### Installation

#### Standalone Version (Recommended)
```bash
# Install dependencies
pip install google-generativeai flask flask-cors

# Update API key in standalone_health_chatbot.py

# Run the app
python standalone_health_chatbot.py
```

#### Full React Version
```bash
# Backend setup
cd health-chatbot-backend
pip install -r requirements.txt
python simple_backend.py

# Frontend setup (new terminal)
cd health-chatbot-frontend
npm install
npm start
```

## 🎯 Usage Examples

### Natural Language Input
- "I have fever and headache"
- "ayurvedic treatment for cold"
- "home remedies for stomach pain"
- "homeopathy for anxiety"

### Treatment Types
- 🌿 **Ayurvedic**: Traditional Indian medicine
- 🌸 **Homeopathy**: Natural alternative medicine
- 🏠 **Home Remedies**: Simple natural treatments

## 🌐 API Endpoints

### Chat Endpoint
```http
POST /chat
Content-Type: application/json

{
  "message": "I have fever and headache"
}
```

### Response
```json
{
  "success": true,
  "response": "🌿 **Ayurvedic Medicine**: Trikatu Churna..."
}
```

## 📱 Screenshots

Coming soon! The chatbot features:
- Modern gradient design
- Real-time typing indicators
- Mobile-responsive layout
- Natural conversation flow

## 🔒 Security & Privacy

- ⚠️ **Medical Disclaimer**: This is for informational purposes only
- 🔐 **API Key**: Keep your Gemini API key private
- 🚫 **No Data Storage**: Conversations are not stored
- 🛡️ **Local Processing**: All processing happens locally

## 🤝 Contributing

Contributions are welcome! Please feel free to:
- 🐛 Report bugs
- 💡 Suggest features
- 📝 Improve documentation
- 🎨 Enhance UI/UX

## 📄 License

This project is open source and available under the MIT License.

## 🙏 Acknowledgments

- **Google Gemini AI** for powering the natural language processing
- **Flask** for the backend framework
- **React** for the frontend framework
- **Bootstrap** for UI components

## 📞 Support

For support or questions:
1. Check the [Issues](https://github.com/Kevin-Zalavadiya/chatbot-AI/issues) page
2. Create a new issue with detailed description
3. Join our community discussions

---

**Made with ❤️ using AI technology** 🤖

---

### 🎉 Quick Test

Want to test it right now?

```bash
# Clone and run in 2 minutes
git clone https://github.com/Kevin-Zalavadiya/chatbot-AI
cd chatbot-AI
pip install google-generativeai flask flask-cors
python standalone_health_chatbot.py
```

Then open `http://localhost:5000` and start chatting! 🚀
