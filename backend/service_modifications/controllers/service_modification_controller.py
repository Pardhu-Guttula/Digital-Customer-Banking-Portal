# Epic Title: Redis Caching for Service Modification Workflows

from flask import Blueprint, request, jsonify
from backend.service_modifications.services.service_modification_service import ServiceModificationService
import logging

service_modification_controller = Blueprint('service_modification_controller', __name__)
service = ServiceModificationService()

logging.basicConfig(level=logging.INFO)
logger = logging.getLogger(__name__)

@service_modification_controller.route('/service_modification', methods=['POST'])
def submit_service_modification():
    data = request.json
    logger.info(f"Received service modification request: {data}")

    if not data.get('service_name') or not data.get('modification_details'):
        return jsonify({'error': 'service_name and modification_details are required fields'}), 400

    try:
        result, error = service.process_request(data)
        if error:
            return jsonify({'error': error}), 400
        return jsonify({'message': 'Service modification request stored successfully'}), 200
    except Exception as e:
        logger.error(f"Error processing service modification request: {e}")
        return jsonify({'error': 'Internal server error'}), 500

@service_modification_controller.route('/service_modification', methods=['GET'])
def get_service_modifications():
    try:
        modifications = service.get_all_requests()
        return jsonify(modifications), 200
    except Exception as e:
        logger.error(f"Error retrieving service modification requests: {e}")
        return jsonify({'error': 'Internal server error'}), 500