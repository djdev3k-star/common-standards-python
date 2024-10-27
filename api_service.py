import os
import requests
from dotenv import load_dotenv

# Load environment variables
load_dotenv('.env')
API_KEY = os.getenv('API_KEY')

# Common headers for requests
HEADERS = {
    'Api-key': API_KEY,
    'Content-Type': 'application/json'
}

# Base URL for the API
BASE_URL = "https://api.commonstandardsproject.com/api/v1"


# Function to fetch jurisdiction data
def get_jurisdictions():
    url = f"{BASE_URL}/jurisdictions"
    try:
        response = requests.get(url, headers=HEADERS)
        response.raise_for_status()
        return response.json().get('data', [])
    except requests.exceptions.RequestException as e:
        print(f"Error fetching jurisdictions: {e}")
        return []


# Function to fetch specific jurisdiction data by ID
def get_jurisdiction_data(jurisdiction_id):
    url = f"{BASE_URL}/jurisdictions/{jurisdiction_id}"
    try:
        response = requests.get(url, headers=HEADERS)
        response.raise_for_status()
        return response.json().get('data', {})
    except requests.exceptions.RequestException as e:
        print(f"Error fetching jurisdiction data for ID {jurisdiction_id}: {e}")
        return {}


# Function to fetch standard details by standard set ID
def get_standard_details(standard_set_id):
    url = f"{BASE_URL}/standard_sets/{standard_set_id}"
    try:
        response = requests.get(url, headers=HEADERS)
        response.raise_for_status()
        return response.json().get('data', {}).get('standards', {})
    except requests.exceptions.RequestException as e:
        print(f"Error fetching standards for standard set ID {standard_set_id}: {e}")
        return {}

