from flask import Flask, request, jsonify
from flask_cors import CORS
import sys
import os

# Add the parent directory to the path so we can import health_chatbot
sys.path.append(os.path.dirname(os.path.abspath(__file__)))

from health_chatbot import HealthChatbot

app = Flask(__name__)
CORS(app)  # Enable CORS for all routes

# Initialize the chatbot
try:
    bot = HealthChatbot("AIzaSyAquFtvl1hpeEWB4AzDploXMyygZwIWqWI")
    print("✅ Chatbot initialized successfully!")
except Exception as e:
    print(f"❌ Failed to initialize chatbot: {e}")
    bot = None

@app.route('/')
def root():
    return jsonify({"message": "Health Chatbot API with Gemini is running!"})

@app.route('/chat', methods=['POST'])
def chat():
    try:
        if not bot:
            return jsonify({
                'success': False,
                'error': 'Chatbot not initialized'
            }), 500
        
        data = request.get_json()
        if not data or 'message' not in data:
            return jsonify({
                'success': False,
                'error': 'Message is required'
            }), 400
        
        user_message = data.get('message', '')
        if not user_message.strip():
            return jsonify({
                'success': False,
                'error': 'Please enter a message'
            }), 400
        
        # Get response from chatbot
        response = bot.chat(user_message)
        
        return jsonify({
            'success': True,
            'response': response
        })
        
    except Exception as e:
        print(f"Error in chat endpoint: {e}")
        return jsonify({
            'success': False,
            'error': str(e)
        }), 500

@app.route('/search_by_symptoms', methods=['GET'])
def search_by_symptoms():
    """Compatibility endpoint for existing frontend"""
    try:
        if not bot:
            return jsonify({
                'error': 'Service temporarily unavailable',
                'hindi_error': 'सेवा अस्थायी रूप से अनुपलब्ध है'
            }), 500
        
        symptoms = request.args.get('symptoms', '')
        treatment_type = request.args.get('treatment_type', 'all')
        
        if not symptoms:
            return jsonify({
                'error': 'Please enter at least 2 symptoms',
                'hindi_error': 'कृपया कम से कम 2 लक्षण दर्ज करें'
            }), 400
        
        # Create user message based on treatment type
        if treatment_type.lower() == 'ayurveda':
            user_message = f"ayurvedic treatment for {symptoms}"
        elif treatment_type.lower() == 'homeopathy':
            user_message = f"homeopathy for {symptoms}"
        elif treatment_type.lower() in ['home_remedy', 'home remedies', 'remedy']:
            user_message = f"home remedies for {symptoms}"
        else:
            user_message = symptoms
        
        # Get response from chatbot
        response = bot.chat(user_message)
        
        # Format response to match frontend expectations
        return jsonify({
            'results': [{
                'disease': 'AI Generated Treatment',
                'type': treatment_type,
                'matched_symptoms': symptoms.split(','),
                'match_count': len(symptoms.split(',')),
                'total_symptoms_searched': len(symptoms.split(',')),
                'medicine': 'AI Generated Treatment',
                'response': response,
                'confidence': 95,
                'dosage': 'AI Generated',
                'precautions': 'AI Generated',
                'home_tips': 'AI Generated'
            }]
        })
        
    except Exception as e:
        print(f"Error in search_by_symptoms endpoint: {e}")
        return jsonify({
            'error': 'Service temporarily unavailable',
            'hindi_error': 'सेवा अस्थायी रूप से अनुपलब्ध है'
        }), 500

if __name__ == '__main__':
    print("🚀 Starting Health Chatbot Backend...")
    print("📍 Server will be available at: http://localhost:8000")
    print("🔗 Frontend should connect to: http://localhost:8000")
    print("=" * 50)
    
    app.run(
        debug=True,
        host='0.0.0.0',
        port=8000,
        threaded=True
    )
