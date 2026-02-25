# Epic Title: User Authentication and Session Management for Secure Login

from flask import Flask
from backend.authentication.controllers.login_controller import login_controller
import logging

app = Flask(__name__)
app.register_blueprint(login_controller, url_prefix='/auth')

logging.basicConfig(level=logging.INFO)
logger = logging.getLogger(__name__)

@app.route('/')
def home():
    return "Welcome to User Authentication System"

if __name__ == '__main__':
    logger.info("Starting the User Authentication System...")
    app.run(debug=True)