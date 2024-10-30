# app.py
from flask import Flask, render_template
from routes.jurisdiction_routes import jurisdiction_bp
from routes.standards_routes import standards_bp
from routes.organizations_routes import organizations_bp  # create this

from dotenv import load_dotenv
import os

# Load environment variables from .env
load_dotenv()

def create_app():
    app = Flask(__name__)

    # Register blueprints
    app.register_blueprint(jurisdiction_bp, url_prefix='/jurisdictions')
    app.register_blueprint(standards_bp, url_prefix='/standards')
    app.register_blueprint(organizations_bp, url_prefix='/organizations')  # Register the new blueprint
    
    @app.route('/')
    def index():
        return render_template('index.html')

    return app

if __name__ == "__main__":
    app = create_app()
    app.run(debug=True)
