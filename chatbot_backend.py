from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from pydantic import BaseModel
from health_chatbot import HealthChatbot

app = FastAPI()

# Enable CORS so frontend can connect
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

# Initialize the chatbot
bot = HealthChatbot("AIzaSyAquFtvl1hpeEWB4AzDploXMyygZwIWqWI")

class SymptomRequest(BaseModel):
    symptoms: str
    treatment_type: str = "all"

@app.get("/")
def root():
    return {"message": "Health Chatbot API with Gemini is running!"}

@app.post("/chat")
def chat_with_bot(request: SymptomRequest):
    try:
        # Create user message based on treatment type
        if request.treatment_type.lower() == "ayurveda":
            user_message = f"ayurvedic treatment for {request.symptoms}"
        elif request.treatment_type.lower() == "homeopathy":
            user_message = f"homeopathy for {request.symptoms}"
        elif request.treatment_type.lower() in ["home_remedy", "home remedies", "remedy"]:
            user_message = f"home remedies for {request.symptoms}"
        else:
            user_message = request.symptoms
        
        # Get response from chatbot
        response = bot.chat(user_message)
        
        return {
            "success": True,
            "response": response,
            "treatment_type": request.treatment_type,
            "symptoms": request.symptoms
        }
        
    except Exception as e:
        return {
            "success": False,
            "error": str(e),
            "message": "Sorry, I encountered an error. Please try again."
        }

@app.get("/search_by_symptoms")
def search_by_symptoms(symptoms: str, treatment_type: str = "all"):
    """Compatibility endpoint for existing frontend"""
    try:
        request = SymptomRequest(symptoms=symptoms, treatment_type=treatment_type)
        result = chat_with_bot(request)
        
        if result["success"]:
            # Format response to match frontend expectations
            return {
                "results": [{
                    "disease": "General Treatment",
                    "type": treatment_type,
                    "matched_symptoms": symptoms.split(","),
                    "match_count": len(symptoms.split(",")),
                    "total_symptoms_searched": len(symptoms.split(",")),
                    "medicine": "AI Generated Treatment",
                    "response": result["response"],
                    "confidence": 100
                }]
            }
        else:
            return {
                "error": "No matching treatments found",
                "hindi_error": "कोई मिलान करने वाले उपचार नहीं मिले"
            }
            
    except Exception as e:
        return {
            "error": "Service temporarily unavailable",
            "hindi_error": "सेवा अस्थायी रूप से अनुपलब्ध है"
        }

if __name__ == "__main__":
    import uvicorn
    uvicorn.run(app, host="0.0.0.0", port=8000)
