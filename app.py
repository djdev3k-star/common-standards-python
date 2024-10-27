import os
from flask import Flask, render_template, jsonify
import requests
from dotenv import load_dotenv

# Load environment variables
load_dotenv('.env')
API_KEY = os.getenv('API_KEY')

app = Flask(__name__)

# Function to fetch jurisdiction data from the API
def get_jurisdiction_data():
    if API_KEY is None:
        return {}

    url = 'https://api.commonstandardsproject.com/api/v1/jurisdictions/49FCDFBD2CF04033A9C347BFA0584DF0'
    headers = {
        'Api-key': API_KEY,
        'Content-Type': 'application/json'
    }
    try:
        response = requests.get(url, headers=headers)
        response.raise_for_status()
        data = response.json()

        if 'data' not in data:
            return {}

        return data['data']  # Return the main data object
    except requests.exceptions.RequestException as e:
        return {}

# Route for the index page
@app.route('/')
def index():
    standard_data = get_jurisdiction_data()
    
    if standard_data:
        standard_sets = standard_data.get('standardSets', [])
    else:
        standard_sets = []

    return render_template('index.html', standard_sets=standard_sets)

# Route to fetch standards for a given standard set ID
@app.route('/standard/<standard_set_id>')
def fetch_standard_details(standard_set_id):
    url = f'https://api.commonstandardsproject.com/api/v1/standard_sets/{standard_set_id}'
    headers = {
        'Api-key': API_KEY,
        'Content-Type': 'application/json'
    }

    try:
        response = requests.get(url, headers=headers)
        response.raise_for_status()
        data = response.json()

        # Access standards as a dictionary of objects
        standards_data = data.get('data', {}).get('standards', {})

        if not standards_data:
            return render_template('standards.html', error="No standards found for this standard set.")

        # Convert standards dictionary to a list of values to make it iterable in the template
        standards_list = list(standards_data.values())

        # Render the template with the list of standards
        return render_template(
            'standards.html', 
            standards=standards_list,
            standard_set_title=data['data'].get('title')
        )
    except requests.exceptions.RequestException as e:
        return render_template('standards.html', error="An error occurred while fetching the data.")


if __name__ == "__main__":
    app.run(debug=True)
