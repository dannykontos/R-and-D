from flask import Flask, render_template
import requests

# Define API URL.
TRIVIA_URL = 'https://api.api-ninjas.com/v1/trivia'

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
        return render_template('index.html', question=trivia['question'], answer=trivia['answer'])
    except requests.exceptions.RequestException as e:
        return f"An error occurred: {e}"
    except (IndexError, KeyError) as e:
        return "No trivia found or invalid response format"

# Run the Flask app (127.0.0.1:5000 by default).
if __name__ == '__main__':
    app.run(debug=True)
