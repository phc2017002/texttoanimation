import os
from google import genai
from dotenv import load_dotenv

load_dotenv()

client = genai.Client(api_key=os.getenv("GEMINI_API_KEY"))

print("Listing models...")
try:
    # The SDK might have a different way to list models, let's try the standard way if possible
    # Or just try to generate with a few known names and see which one doesn't error immediately
    # But wait, the SDK documentation should be followed.
    # Since I don't have the docs, I'll try to use the client to list models if a method exists.
    # Based on previous error "Call ListModels to see the list...", it suggests such a method exists.
    # Let's try client.models.list()
    
    for model in client.models.list():
        print(model.name)
        
except Exception as e:
    print(f"Error listing models: {e}")
