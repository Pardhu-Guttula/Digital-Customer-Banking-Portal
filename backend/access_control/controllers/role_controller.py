# Epic Title: Implement role-based access control for user authorization

from flask import Blueprint, request, jsonify
from backend.access_control.services.role_service import RoleService
from backend.database.config import get_db

role_bp = Blueprint('role', __name__)

@role_bp.route('/roles', methods=['POST'])
def create_role():
    db = next(get_db())
    data = request.get_json()

    role_service = RoleService(db)
    
    try:
        role_service.create_role(data)
        return jsonify({"message": "Role created successfully"}), 201
    except Exception as e:
        return jsonify({"error": str(e)}), 400

@role_bp.route('/roles', methods=['GET'])
def get_roles():
    db = next(get_db())

    role_service = RoleService(db)
    
    roles = role_service.get_roles()
    return jsonify({"roles": roles}), 200