from flask import Flask, render_template, request, redirect, url_for, jsonify
import requests
from dotenv import load_dotenv
import os

# Initialize the Flask app
app = Flask(__name__)

# Load environment variables
load_dotenv('.env')
API_KEY = os.getenv('API_KEY')

# Function to fetch jurisdiction data from the API
def get_data():
    if API_KEY is None:
        return {"error": "API_KEY not found. Please set the API_KEY in your .env file."}

    url = 'https://api.commonstandardsproject.com/api/v1/jurisdictions/49FCDFBD2CF04033A9C347BFA0584DF0'
    headers = {
        'Api-key': API_KEY,
        'Content-Type': 'application/json'
    }
    try:
        response = requests.get(url, headers=headers)
        response.raise_for_status()
        data = response.json()

        # Check if 'data' key exists
        if 'data' not in data:
            return {"error": "API response does not contain 'data'."}

        return data['data']  # Return the main data object
    except requests.exceptions.RequestException as e:
        return {"error": f"An error occurred: {e}"}
    except KeyError:
        return {"error": "Unexpected response structure. Please check the API response."}

# Route to display the main page with standard sets
@app.route('/')
def index():
    # Fetch data from the API
    standard_data = get_data()
    
    # Check if there was an error in fetching data
    if "error" in standard_data:
        return standard_data["error"]

    # Prepare the list of standard sets for display
    standard_sets = []
    if 'standardSets' in standard_data:
        for standard_set in standard_data['standardSets']:
            standard_sets.append({
                "id": standard_set.get("id"),
                "title": standard_set.get("title", "No Title"),
                "subject": standard_set.get("subject", "No Subject")
            })

    # Render the HTML template and pass the standard sets data
    return render_template('index.html', standard_sets=standard_sets)

# Route to fetch additional data for a selected standard set
@app.route('/standard/<standard_set_id>')
def fetch_additional_data(standard_set_id):
    # Endpoint to fetch additional details for a specific standard set
    url = f'https://api.commonstandardsproject.com/api/v1/standards/{standard_set_id}'
    
    headers = {
        'Api-key': API_KEY,
        'Content-Type': 'application/json'
    }
    
    try:
        response = requests.get(url, headers=headers)
        response.raise_for_status()
        data = response.json()

        # Check if the data returned is as expected
        if 'data' not in data:
            return jsonify({"error": f"No data found for Standard Set ID {standard_set_id}"})
        
        # Prepare the standards details for display
        standards_data = data['data'].get('standards', {})
        standards_list = []
        for standard_id, standard in standards_data.items():
            standards_list.append({
                "id": standard_id,
                "description": standard.get('description', 'No Description Available')
            })

        return jsonify({"standards": standards_list})

    except requests.exceptions.RequestException as e:
        return jsonify({"error": f"An error occurred when fetching data for {standard_set_id}: {e}"})

# Run the Flask app
if __name__ == "__main__":
    app.run(debug=True)
