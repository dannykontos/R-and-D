from flask import Flask, render_template, request, jsonify
import requests

# Define API URLs.
TRIVIA_URL = 'https://api.api-ninjas.com/v1/trivia'
EXERCISES_URL = 'https://api.api-ninjas.com/v1/exercises'

# Initialize Flask.
app = Flask(__name__)

# Define routing.
@app.route('/')
def index():
    try:
        # Make API Call - make sure to use a valid API key.
        response = requests.get(TRIVIA_URL, headers={'X-Api-Key': '4YbGrNcrjhUKVE1ZVZtw6A==dO8jueewFyOBZE2K'})
        response.raise_for_status()  # Raise an exception for HTTP errors
        resp = response.json()

        # Get first trivia result since the API returns a list of results.
        trivia = resp[0]

        # Render HTML using the trivia question and answer.
        return render_template('index-danny.html', question=trivia['question'], answer=trivia['answer'])
    except requests.exceptions.RequestException as e:
        return f"An error occurred: {e}"
    except (IndexError, KeyError) as e:
        return "No trivia found or invalid response format"

@app.route('/get_workout', methods=['POST'])
def get_workout():
    exercise_type = request.json.get('exercise_type')
    muscle_group = request.json.get('muscle_group')
    
    if not exercise_type and not muscle_group:
        return jsonify({"error": "At least one parameter (exercise type or muscle group) is required"}), 400
    
    params = {}
    if exercise_type:
        params['type'] = exercise_type
    if muscle_group:
        params['muscle'] = muscle_group

    try:
        # Make API Call - make sure to use a valid API key.
        response = requests.get(EXERCISES_URL,
                                headers={'X-Api-Key': '4YbGrNcrjhUKVE1ZVZtw6A==dO8jueewFyOBZE2K'},
                                params=params)
        response.raise_for_status()  # Raise an exception for HTTP errors
        exercises = response.json()

        # Return the exercises as JSON.
        return jsonify(exercises)
    except requests.exceptions.RequestException as e:
        return jsonify({"error": str(e)}), 500

# Run the Flask app (127.0.0.1:5000 by default).
if __name__ == '__main__':
    app.run(debug=True)
