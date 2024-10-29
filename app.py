import os
from flask import Flask
from dotenv import load_dotenv

# Import blueprints
from routes.main_routes import main_bp
from routes.standards_routes import standards_bp

load_dotenv('.env')
API_KEY = os.getenv('API_KEY')

app = Flask(__name__)

# Register blueprints
app.register_blueprint(main_bp)
app.register_blueprint(standards_bp, url_prefix='/standards')

if __name__ == "__main__":
    app.run(debug=True)
