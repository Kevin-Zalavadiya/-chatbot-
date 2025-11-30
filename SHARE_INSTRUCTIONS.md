# 🌿 Gemini Health Chatbot - Share Package

## 📁 Files to Share

### Backend (Python)
- `health_chatbot.py` - Core chatbot with Gemini API
- `simple_backend.py` - Flask server
- `requirements.txt` - Python packages

### Frontend (React)
- `src/components/GeminiChatbot.js` - Chat interface
- `src/components/GeminiChatbot.css` - Beautiful styling
- `src/App.js` - Main app
- `package.json` - Node dependencies

## 🚀 Setup Instructions

### 1. Backend Setup
```bash
# Install Python dependencies
pip install -r requirements.txt

# Start the backend server
python simple_backend.py
```

### 2. Frontend Setup
```bash
# Install Node dependencies
npm install

# Start the frontend
npm start
```

### 3. Access the Chatbot
- Frontend: http://localhost:3000
- Backend API: http://localhost:8000

## 🔑 API Key Required
Update the API key in:
- `health_chatbot.py` (line 126)
- `simple_backend.py` (line 18)

Replace: `AIzaSyAquFtvl1hpeEWB4AzDploXMyygZwIWqWI` with your key.

## ✨ Features
- 🌿 Natural symptom input (no CSV restrictions)
- 🤖 Gemini AI-powered responses
- 🎨 Beautiful modern UI
- 📱 Mobile responsive
- 🌸 Multiple treatment types (Ayurvedic, Homeopathy, Home Remedies)
- 🌍 Multi-language support (English/Hindi)

## 🎯 What It Does
- Users describe symptoms naturally
- AI extracts symptoms automatically
- Returns clean, formatted treatment recommendations
- Professional medical disclaimers included

## 📞 Support
Built with Gemini AI + React + Flask
No CSV files needed - everything AI-powered!
