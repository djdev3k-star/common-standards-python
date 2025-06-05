# routes/standards_routes.py
from flask import Blueprint, render_template
from api_service import get_standard_set_details

standards_bp = Blueprint('standards', __name__)

@standards_bp.route('/<standard_set_id>')
def fetch_standard_details(standard_set_id):
    standard_set = get_standard_set_details(standard_set_id)
    standards = standard_set.get('standards', {}).values()  # Convert to list
    return render_template('standards.html', standard_set=standard_set, standards=standards)
