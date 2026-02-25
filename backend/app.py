# Epic Title: Personalized User Dashboard for Banking Products and Services

from flask import Flask
from backend.dashboard.controllers.dashboard_controller import dashboard_controller
import logging

app = Flask(__name__)
app.register_blueprint(dashboard_controller, url_prefix='/api')

logging.basicConfig(level=logging.INFO)
logger = logging.getLogger(__name__)

@app.route('/')
def home():
    return "Welcome to the Personalized Banking Dashboard"

if __name__ == '__main__':
    logger.info("Starting the Personalized Banking Dashboard System...")
    app.run(debug=True)