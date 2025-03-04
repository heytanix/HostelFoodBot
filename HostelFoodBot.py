from flask import Flask, jsonify, send_from_directory, request
from flask_cors import CORS
from google import genai
from dotenv import load_dotenv
import os
import random

# Loading the environment variables from ".env" file
load_dotenv()

app = Flask(__name__, static_folder='.')  # Specify static folder as current directory
CORS(app)  # Enable CORS for all routes

# Initialize the GenAI client with the API key
api_key = os.getenv("API_KEY")  # Load API key from environment variable
client = genai.Client(api_key=api_key)

def get_joke():
    # List of topics for jokes
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
    
    # Randomly select a topic
    selected_topic = random.choice(topics)
    
    # General prompt to generate a random joke
    prompt = f"Tell me a funny joke about {selected_topic} in a complete sentence."
    
    # Generation of content using the Gemini-2.0-Flash model
    response = client.models.generate_content(
        model="gemini-2.0-flash", 
        contents=f"{prompt} | The rules are: 1. The joke should be funny, 2. The joke should not contain dark humor, 3. The joke should not be offensive, 4. The joke should not contain NSFW content"
    )
    
    # Debugging: Print the raw response
    print("Raw response from GenAI:", response.text)
    
    # Assuming the response contains the joke in a specific format
    jokes = response.text.strip().split('\n')  # Split by new lines if multiple jokes are returned
    unique_jokes = list(set(jokes))  # Remove duplicates by converting to a set
    
    # Debugging: Print the unique jokes
    print("Unique jokes generated:", unique_jokes)
    
    # Return a random unique joke, ensuring it's a single string
    return random.choice(unique_jokes).strip() if unique_jokes else "No joke found."

def get_recipe(ingredients, dietary_preference):
    # Example implementation for recipe suggestion based on ingredients
    # This should ideally call the GenAI model to get recipes based on user input
    prompt = f"Suggest a budget-friendly Indian recipe using the following ingredients: {', '.join(ingredients)}. Dietary preference: {dietary_preference}."
    
    response = client.models.generate_content(
        model="gemini-2.0-flash", 
        contents=prompt
    )
    
    # Debugging: Print the raw response
    print("Raw response from GenAI for recipe:", response.text)
    
    return response.text.strip()  # Return the recipe suggestion

@app.route('/')
def home():
    return send_from_directory(app.static_folder, 'index.html')  # Serve index.html from static folder

@app.route('/get_joke', methods=['GET'])
def fetch_joke():
    joke = get_joke()  # Get a random joke
    return jsonify({"joke": joke})  # Return the joke as a JSON response

@app.route('/get_recipe', methods=['POST'])
def fetch_recipe():
    data = request.json  # Get JSON data from the request
    ingredients = data.get('ingredients', [])
    dietary_preference = data.get('dietary_preference', 'vegetarian')  # Default to vegetarian
    recipe = get_recipe(ingredients, dietary_preference)  # Get a recipe based on ingredients
    return jsonify({"recipe": recipe})  # Return the recipe as a JSON response

@app.route('/<path:filename>', methods=['GET'])
def serve_static(filename):
    return send_from_directory(app.static_folder, filename)  # Serve static files (CSS, etc.)

if __name__ == "__main__":
    app.run(host='0.0.0.0', port=5000, debug=True)  # Run the Flask app in debug mode
