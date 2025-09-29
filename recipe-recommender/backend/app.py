from flask import Flask, request, jsonify
from flask_cors import CORS
from logic import suggests_recipes

app = Flask(__name__)
CORS(app)

@app.route('/')
def home():
    return "Recipe Recommender API is running!"

@app.route('/recommend', methods=['POST'])
def recommend():
    data = request.json
    ingredients = data.get('ingredients', [])
    recipes = suggests_recipes(ingredients)
    return jsonify(recipes)
if __name__ == '__main__':
    app.run(debug=True, port=5000)  # Change to 5001


