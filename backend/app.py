# Epic Title: Frontend Account Opening Workflow Using React

from flask import Flask, request, jsonify
import logging

app = Flask(__name__)

logging.basicConfig(level=logging.INFO)
logger = logging.getLogger(__name__)

@app.route('/')
def home():
    return "Welcome to the Account Opening Workflow"

@app.route('/submit_account_opening', methods=['POST'])
def submit_account_opening():
    data = request.json
    # Placeholder for actual logic
    required_fields = ['name', 'email', 'phone', 'address']
    for field in required_fields:
        if field not in data or not data[field]:
            return jsonify({'error': f'{field} is required'}), 400

    logger.info(f"Account opening request submitted: {data}")
    return jsonify({'message': 'Account opening request submitted successfully'}), 200

if __name__ == '__main__':
    logger.info("Starting the Account Opening Workflow System...")
    app.run(debug=True)