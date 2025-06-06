from flask import Blueprint, render_template, request
from api_service import get_jurisdictions, get_jurisdiction_details

jurisdiction_bp = Blueprint('jurisdictions', __name__)

@jurisdiction_bp.route('/')
def jurisdictions_home():
    search_query = request.args.get('search', '').lower()
    jurisdictions = get_jurisdictions()
    
    if search_query:
        jurisdictions = [j for j in jurisdictions if search_query in j['title'].lower()]

    return render_template('jurisdictions.html', 
                         jurisdictions=jurisdictions,
                         jurisdiction=None,
                         standard_sets=None)

@jurisdiction_bp.route('/<jurisdiction_id>')
def view_jurisdiction(jurisdiction_id):
    jurisdiction_data = get_jurisdiction_details(jurisdiction_id)
    standard_sets = jurisdiction_data.get('standardSets', [])
    
    return render_template('jurisdictions.html',
                         jurisdiction=jurisdiction_data,
                         standard_sets=standard_sets,
                         jurisdictions=[])