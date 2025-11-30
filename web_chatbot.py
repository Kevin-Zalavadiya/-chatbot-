from flask import Flask, render_template, request, jsonify
from health_chatbot import HealthChatbot

app = Flask(__name__)

# Initialize the chatbot
bot = HealthChatbot("AIzaSyAquFtvl1hpeEWB4AzDploXMyygZwIWqWI")

@app.route('/')
def home():
    return render_template('index.html')

@app.route('/chat', methods=['POST'])
def chat():
    try:
        user_message = request.json.get('message', '')
        if not user_message:
            return jsonify({'error': 'Please enter a message'})
        
        # Get response from chatbot
        response = bot.chat(user_message)
        
        return jsonify({
            'success': True,
            'response': response
        })
        
    except Exception as e:
        return jsonify({
            'success': False,
            'error': str(e)
        })

if __name__ == '__main__':
    app.run(debug=True, host='0.0.0.0', port=5000)
