from flask import Blueprint, render_template, request
from api_service import get_jurisdictions  # Import the API service function

main_bp = Blueprint('main', __name__)

# Landing page route
@main_bp.route('/')
def landing_page():
    return render_template('landing.html')

# Search page route
@main_bp.route('/search')
def search_jurisdictions():
    query = request.args.get('q', '').lower()
    jurisdictions = get_jurisdictions()
    # Filter results by matching the query with title or type
    filtered_jurisdictions = [
        j for j in jurisdictions if query in j['title'].lower() or query in j['type'].lower()
    ]
    return render_template('search_results.html', jurisdictions=filtered_jurisdictions, query=query)
