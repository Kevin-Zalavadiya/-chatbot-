import google.generativeai as genai

# Configure with your API key
genai.configure(api_key="AIzaSyAquFtvl1hpeEWB4AzDploXMyygZwIWqWI")

# List available models
print("Available models:")
for model in genai.list_models():
    if 'generateContent' in model.supported_generation_methods:
        print(model.name)
