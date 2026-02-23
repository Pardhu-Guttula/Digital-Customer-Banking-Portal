# Epic Title: User Authentication and Authorization

from flask import Blueprint, request, jsonify
from pydantic import ValidationError
from backend.authentication.models.password_recovery import PasswordRecovery
from backend.authentication.services.password_recovery_service import PasswordRecoveryService

password_recovery_bp = Blueprint('password_recovery', __name__)

@password_recovery_bp.route('/password-recovery', methods=['POST'])
def recover_password():
    try:
        recovery_data = request.json
        recovery_details = PasswordRecovery(**recovery_data)
        success = PasswordRecoveryService.send_recovery_email(recovery_details.email)
        if success:
            return jsonify({"message": "Password recovery email sent"}), 200
        else:
            return jsonify({"error": "Email not recognized"}), 400
    except ValidationError as e:
        return jsonify({"errors": e.errors()}), 400
