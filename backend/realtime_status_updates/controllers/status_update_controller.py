# Epic Title: Real-time Status Updates Using React and Redis

from flask import Blueprint, jsonify
from backend.realtime_status_updates.services.status_update_service import StatusUpdateService
import logging

status_update_controller = Blueprint('status_update_controller', __name__)
service = StatusUpdateService()

logging.basicConfig(level=logging.INFO)
logger = logging.getLogger(__name__)

@status_update_controller.route('/status/<int:request_id>', methods=['GET'])
def get_status_update(request_id):
    logger.info(f"Fetching status update for request ID: {request_id}")
    try:
        status = service.get_status_from_cache(request_id)
        if status is None:
            status = service.get_status_from_db(request_id)
        return jsonify({'request_id': request_id, 'status': status}), 200
    except Exception as e:
        logger.error(f"Error fetching status update: {e}")
        return jsonify({'error': 'Internal server error'}), 500