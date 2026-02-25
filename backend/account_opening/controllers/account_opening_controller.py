# Epic Title: PostgreSQL Data Storage for Account Opening Requests

from flask import Blueprint, request, jsonify
from backend.account_opening.services.account_opening_service import AccountOpeningService
import logging

account_opening_controller = Blueprint('account_opening_controller', __name__)
service = AccountOpeningService()

logging.basicConfig(level=logging.INFO)
logger = logging.getLogger(__name__)

@account_opening_controller.route('/account_opening', methods=['POST'])
def submit_account_opening():
    data = request.json
    logger.info(f"Received account opening request: {data}")
    
    try:
        result, error = service.process_request(data)
        if error:
            return jsonify({'error': error}), 400
        return jsonify({'message': 'Account opening request stored successfully'}), 200
    except Exception as e:
        logger.error(f"Error processing account opening request: {e}")
        return jsonify({'error': 'Internal server error'}), 500