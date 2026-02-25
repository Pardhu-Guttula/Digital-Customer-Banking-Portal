# Epic Title: React UI for Service Modification Requests

from flask import Flask
from backend.service_modifications.controllers.service_modification_controller import service_modification_controller
import logging

app = Flask(__name__)
app.register_blueprint(service_modification_controller, url_prefix='/api')

logging.basicConfig(level=logging.INFO)
logger = logging.getLogger(__name__)

@app.route('/')
def home():
    return "Welcome to the Service Modification System"

if __name__ == '__main__':
    logger.info("Starting the Service Modification System...")
    app.run(debug=True)