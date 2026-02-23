# Epic Title: Save incomplete application state

from flask import Blueprint, request, jsonify
from backend.application.services.application_state_service import ApplicationStateService
from backend.database.config import get_db

application_state_bp = Blueprint('application_state', __name__)

@application_state_bp.route('/state/save', methods=['POST'])
def save_application_state():
    db = next(get_db())
    data = request.get_json()

    application_state_service = ApplicationStateService(db)
    
    try:
        application_state_service.save_state(data)
        return jsonify({"message": "Application state saved successfully"}), 200
    except Exception as e:
        return jsonify({"error": str(e)}), 500

@application_state_bp.route('/state/load', methods=['GET'])
def load_application_state():
    db = next(get_db())
    user_id = request.args.get('user_id')

    application_state_service = ApplicationStateService(db)
    
    try:
        state = application_state_service.load_state(user_id)
        return jsonify({"state": state}), 200
    except Exception as e:
        return jsonify({"error": str(e)}), 500