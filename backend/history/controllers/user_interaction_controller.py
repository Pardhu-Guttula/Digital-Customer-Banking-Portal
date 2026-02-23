# Epic Title: Capture and maintain a history of user interactions

from flask import Blueprint, request, jsonify
from backend.history.services.user_interaction_service import UserInteractionService
from backend.database.config import get_db

user_interaction_bp = Blueprint('user_interaction', __name__)

@user_interaction_bp.route('/interaction/record', methods=['POST'])
def record_interaction():
    db = next(get_db())
    data = request.get_json()

    user_interaction_service = UserInteractionService(db)
    
    try:
        user_interaction_service.record_interaction(data)
        return jsonify({"message": "User interaction recorded successfully"}), 200
    except Exception as e:
        return jsonify({"error": str(e)}), 500