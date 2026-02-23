# Epic Title: Implement role-based access control for user authorization

from flask import Blueprint, request, jsonify
from backend.access_control.services.permission_service import PermissionService
from backend.database.config import get_db

permission_bp = Blueprint('permission', __name__)

@permission_bp.route('/permissions', methods=['POST'])
def assign_permission_to_role():
    db = next(get_db())
    data = request.get_json()

    permission_service = PermissionService(db)
    
    try:
        permission_service.assign_permission(data)
        return jsonify({"message": "Permissions assigned successfully"}), 200
    except Exception as e:
        return jsonify({"error": str(e)}), 400