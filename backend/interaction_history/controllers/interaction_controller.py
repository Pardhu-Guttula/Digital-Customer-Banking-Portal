# Epic Title: Store User Interaction Data in PostgreSQL

from flask import Blueprint, request, jsonify
from backend.interaction_history.services.interaction_service import InteractionService
import logging

interaction_controller = Blueprint('interaction_controller', __name__)
service = InteractionService()

logging.basicConfig(level=logging.INFO)
logger = logging.getLogger(__name__)

@interaction_controller.route('/interactions', methods=['POST'])
def store_interaction():
    data = request.json
    logger.info(f"Received interaction data: {data}")

    if not data.get('user_id') or not data.get('interaction_type'):
        return jsonify({'error': 'user_id and interaction_type are required fields'}), 400

    try:
        service.store_interaction(data)
        return jsonify({'message': 'Interaction data stored successfully'}), 200
    except Exception as e:
        logger.error(f"Error storing interaction data: {e}")
        return jsonify({'error': 'Internal server error'}), 500

@interaction_controller.route('/interactions/<int:user_id>', methods=['GET'])
def get_interactions(user_id: int):
    try:
        interactions = service.get_interactions_by_user(user_id)
        return jsonify(interactions), 200
    except Exception as e:
        logger.error(f"Error retrieving interactions: {e}")
        return jsonify({'error': 'Internal server error'}), 500