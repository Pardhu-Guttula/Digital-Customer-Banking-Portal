# Epic Title: React UI for Service Modification Requests

from flask import Blueprint, request, jsonify
import logging

service_modification_controller = Blueprint('service_modification_controller', __name__)

logging.basicConfig(level=logging.INFO)
logger = logging.getLogger(__name__)

@service_modification_controller.route('/service_modification', methods=['POST'])
def submit_service_modification():
    data = request.json
    logger.info(f"Received service modification request: {data}")
    
    # Validate input data
    if not data.get('service_name') or not data.get('modification_details'):
        return jsonify({'error': 'service_name and modification_details are required fields'}), 400
    
    # Simulate successful storage and response
    try:
        return jsonify({'message': 'Service modification request submitted successfully'}), 200
    except Exception as e:
        logger.error(f"Error processing service modification request: {e}")
        return jsonify({'error': 'Internal server error'}), 500