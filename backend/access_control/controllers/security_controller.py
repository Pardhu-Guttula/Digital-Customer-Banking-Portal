# Epic Title: Security Measures for API Integration

from flask import Blueprint, request, jsonify
from backend.access_control.services.security_service import SecurityService
from backend.database.config import get_db

security_bp = Blueprint('security', __name__)

@security_bp.route('/secure-api', methods=['POST'])
def secure_api_call():
    db = next(get_db())
    token = request.headers.get('Authorization')
    data = request.get_json()

    security_service = SecurityService(db)
    
    try:
        security_service.validate_token(token)
        security_service.encrypt_sensitive_data(data)
        return jsonify({"message": "Interaction authorized and data encrypted"}), 200
    except Exception as e:
        return jsonify({"error": str(e)}), 403
