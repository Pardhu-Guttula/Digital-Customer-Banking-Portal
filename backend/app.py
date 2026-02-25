# Epic Title: Develop Responsive Design for the Portal Using React

from flask import Flask
import logging

app = Flask(__name__)

logging.basicConfig(level=logging.INFO)
logger = logging.getLogger(__name__)

@app.route('/')
def home():
    return "Welcome to the Responsive Portal"

if __name__ == '__main__':
    logger.info("Starting the Responsive Portal System...")
    app.run(debug=True)