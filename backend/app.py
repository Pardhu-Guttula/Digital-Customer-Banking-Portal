# Epic Title: PostgreSQL Data Storage for Account Opening Requests

from flask import Flask
from backend.account_opening.controllers.account_opening_controller import account_opening_controller
import logging

app = Flask(__name__)
app.register_blueprint(account_opening_controller, url_prefix='/api')

logging.basicConfig(level=logging.INFO)
logger = logging.getLogger(__name__)

@app.route('/')
def home():
    return "Welcome to the Account Opening System"

if __name__ == '__main__':
    logger.info("Starting the Account Opening System...")
    app.run(debug=True)