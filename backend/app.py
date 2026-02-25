# Epic Title: Develop a Feature in React for Users to Access Interaction History

from flask import Flask
from backend.interaction_history.controllers.interaction_controller import interaction_controller
import logging

app = Flask(__name__)
app.register_blueprint(interaction_controller, url_prefix='/api')

logging.basicConfig(level=logging.INFO)
logger = logging.getLogger(__name__)

@app.route('/')
def home():
    return "Welcome to the User Interaction Service"

if __name__ == '__main__':
    logger.info("Starting the User Interaction Service...")
    app.run(debug=True)