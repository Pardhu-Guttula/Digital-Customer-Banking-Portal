# Epic Title: Implement role-based access control for user authorization

from flask import Blueprint, request, jsonify
from backend.access_control.services.user_service import UserService
from backend.database.config import get_db

user_bp = Blueprint('user', __name__)

@user_bp.route('/users/<user_id>/role', methods=['POST'])
def assign_role_to_user(user_id):
    db = next(get_db())
    data = request.get_json()

    user_service = UserService(db)
    
    try:
        user_service.assign_role(user_id, data)
        return jsonify({"message": "Role assigned to user successfully"}), 200
    except Exception as e:
        return jsonify({"error": str(e)}), 400

@user_bp.route('/users/<user_id>/permissions', methods=['GET'])
def get_user_permissions(user_id):
    db = next(get_db())

    user_service = UserService(db)
    
    permissions = user_service.get_user_permissions(user_id)
    return jsonify({"permissions": permissions}), 200