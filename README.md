🍳 Recipe Recommender
✨ Features
Smart Recipe Suggestions: Uses algorithms to recommend recipes based on available ingredients
Ingredient Gap Analysis: Shows which ingredients are missing for each recipe
Substitution Recommendations: Suggests alternatives for missing ingredients
Beautiful UI: Modern, responsive design with colors and images
Real-time Updates: Live reloading during development
Cross-platform: Works on Windows, macOS, and Linux
🧱 Tech Stack
Frontend: React.js with modern hooks and styling
Backend: Flask (Python) with CORS support
Database: SQLite for lightweight data storage
Algorithms: Graph theory, backtracking, and greedy algorithms for recipe matching
🚀 Quick Start
Prerequisites
Python 3.7+
Node.js 14+
npm or yarn
1. Clone and Setup
cd "c:/Users/patur/OneDrive/Desktop/daa project 2"
cd recipe-recommender

cd backend
python db_setup.py  # Creates database with sample recipes
python app.py        # Starts Flask server on http://localhost:5000

cd ../frontend
npm install          # Installs React dependencies
npm start            # Starts React server on http://localhost:3000
