# api_service.py
import requests
import os

API_KEY = os.getenv('API_KEY')
BASE_URL = 'https://api.commonstandardsproject.com/api/v1/'

def get_jurisdictions():
    """Fetches all jurisdictions."""
    url = f'{BASE_URL}jurisdictions'
    headers = {'Api-key': API_KEY, 'Content-Type': 'application/json'}
    response = requests.get(url, headers=headers)
    return response.json().get('data', [])

def get_jurisdiction_details(jurisdiction_id):
    """Fetches details for a specific jurisdiction."""
    url = f'{BASE_URL}jurisdictions/{jurisdiction_id}'
    headers = {'Api-key': API_KEY, 'Content-Type': 'application/json'}
    response = requests.get(url, headers=headers)
    return response.json().get('data', {})

def get_standard_set_details(standard_set_id):
    """Fetches details for a specific standard set."""
    url = f'{BASE_URL}standard_sets/{standard_set_id}'
    headers = {'Api-key': API_KEY, 'Content-Type': 'application/json'}
    response = requests.get(url, headers=headers)
    return response.json().get('data', {})
