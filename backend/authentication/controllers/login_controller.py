# Epic Title: User Login

from flask import Blueprint, request, jsonify
from pydantic import ValidationError
from backend.authentication.models.login import Login
from backend.authentication.services.login_service import LoginService

login_bp = Blueprint('login', __name__)

@login_bp.route('/login', methods=['POST'])
def login_user():
    try:
        login_data = request.json
        login_details = Login(**login_data)
        user = LoginService.authenticate(login_details)
        if user:
            return jsonify({"message": "Login successful"}), 200
        else:
            return jsonify({"error": "Invalid credentials"}), 401
    except ValidationError as e:
        return jsonify({"errors": e.errors()}), 400