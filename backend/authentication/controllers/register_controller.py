# Epic Title: User Registration

from flask import Blueprint, request, jsonify
from pydantic import ValidationError
from backend.authentication.models.user import User
from backend.authentication.services.registration_service import RegistrationService

register_bp = Blueprint('register', __name__)

@register_bp.route('/register', methods=['POST'])
def register_user():
    try:
        user_data = request.json
        user = User(**user_data)
        RegistrationService.register_user(user)
        return jsonify({"message": "User successfully registered"}), 201
    except ValidationError as e:
        return jsonify({"errors": e.errors()}), 400