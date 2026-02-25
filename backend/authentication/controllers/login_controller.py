# Epic Title: User Authentication and Session Management for Secure Login

from flask import Blueprint, request, jsonify
from backend.authentication.services.authentication_service import AuthenticationService
from backend.authentication.models.user import User
import logging

login_controller = Blueprint('login_controller', __name__)
auth_service = AuthenticationService()

logging.basicConfig(level=logging.INFO)
logger = logging.getLogger(__name__)

@login_controller.route('/login', methods=['POST'])
def login():
    data = request.json
    logger.info("Login attempt with provided credentials.")
    email = data.get('email')
    password = data.get('password')
    
    if not email or not password:
        logger.error("Email or password not provided.")
        return jsonify({'error': 'Email and password are required'}), 400

    user = auth_service.authenticate(email, password)
    if user:
        token = auth_service.generate_session_token(user)
        logger.info(f"User {email} logged in successfully.")
        return jsonify({'message': 'Login successful', 'token': token}), 200
    else:
        logger.warning(f"Invalid login attempt for email {email}.")
        return jsonify({'error': 'Invalid credentials'}), 401

@login_controller.route('/validate', methods=['POST'])
def validate():
    data = request.json
    email = data.get('email')
    
    if '@' not in email:
        return jsonify({'error': 'Invalid email format'}), 400
    
    return jsonify({'message': 'Valid email format'}), 200