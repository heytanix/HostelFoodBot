from flask import Flask, jsonify, send_from_directory, request
from flask_cors import CORS
from google import genai
from dotenv import load_dotenv
import os
import random

load_dotenv()

app = Flask(__name__, static_folder='.')
CORS(app)

api_key = os.getenv("API_KEY")
client = genai.Client(api_key=api_key)

def get_joke():
    topics = [
        "animals",
        "sports",
        "food",
        "technology",
        "travel",
        "music",
        "movies",
        "science",
        "history",
        "books"
    ]
    
    selected_topic = random.choice(topics)
    
    prompt = f"Tell me a funny joke about {selected_topic} in a complete sentence."
    
    response = client.models.generate_content(
        model="gemini-2.0-flash", 
        contents=f"{prompt} | The rules are: 1. The joke should be funny, 2. The joke should not contain dark humor, 3. The joke should not be offensive, 4. The joke should not contain NSFW content"
    )
    
    print("Raw response from GenAI:", response.text)
    
    jokes = response.text.strip().split('\n')
    unique_jokes = list(set(jokes))
    
    print("Unique jokes generated:", unique_jokes)
    
    return random.choice(unique_jokes).strip() if unique_jokes else "No joke found."

def get_recipe(ingredients, dietary_preference):
    prompt = f"Suggest a budget-friendly Indian recipe using the following ingredients: {', '.join(ingredients)}. Dietary preference: {dietary_preference}."
    
    response = client.models.generate_content(
        model="gemini-2.0-flash", 
        contents=prompt
    )
    
    print("Raw response from GenAI for recipe:", response.text)
    
    return response.text.strip()

@app.route('/')
def home():
    return send_from_directory(app.static_folder, 'index.html')

@app.route('/get_joke', methods=['GET'])
def fetch_joke():
    joke = get_joke()
    return jsonify({"joke": joke})

@app.route('/get_recipe', methods=['POST'])
def fetch_recipe():
    data = request.json
    ingredients = data.get('ingredients', [])
    dietary_preference = data.get('dietary_preference', 'vegetarian')
    recipe = get_recipe(ingredients, dietary_preference)
    return jsonify({"recipe": recipe})

@app.route('/<path:filename>', methods=['GET'])
def serve_static(filename):
    return send_from_directory(app.static_folder, filename)

if __name__ == "__main__":
    app.run(host='0.0.0.0', port=5000, debug=True)
