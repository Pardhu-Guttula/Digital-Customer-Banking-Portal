# Epic Title: Test Portal Usability on Various Screen Sizes

from flask import Flask
import logging

app = Flask(__name__)

logging.basicConfig(level=logging.INFO)
logger = logging.getLogger(__name__)

@app.route('/')
def home():
    return "Welcome to the Responsive Portal"

if __name__ == '__main__':
    logger.info("Starting the Portal Usability Testing System...")
    app.run(debug=True)