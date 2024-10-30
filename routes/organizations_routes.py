# jurisdiction_routes.py
from flask import Blueprint, render_template
from api_service import get_jurisdictions  # Assuming this function gets all jurisdictions

organizations_bp = Blueprint('organizations', __name__)

@organizations_bp.route('/schools_and_organizations')
def schools_and_organizations():
    jurisdictions = get_jurisdictions()  # returns all jurisdictions
    organizations = [j for j in jurisdictions if j['type'] == 'organization']
    schools = [j for j in jurisdictions if j['type'] == 'school']

    return render_template('schools_and_organizations.html', organizations=organizations, schools=schools)
