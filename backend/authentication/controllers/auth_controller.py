# Epic Title: Secure Login System with MFA

from flask import Blueprint, request, jsonify
from sqlalchemy.exc import SQLAlchemyError
from backend.database.config import get_db
from backend.authentication.repositories.account_repository import AccountRepository
from backend.authentication.repositories.mfa_repository import MFARepository
from backend.authentication.services.mfa_service import MFAService

auth_bp = Blueprint('auth', __name__)

@auth_bp.route('/login', methods=['POST'])
def login():
    db = next(get_db())
    data = request.get_json()

    email = data.get('email')
    password = data.get('password')

    account_repository = AccountRepository(db)
    account = account_repository.validate_login(email, password)
    
    if not account:
        return jsonify({"error": "Invalid credentials"}), 401

    mfa_service = MFAService(MFARepository(db))
    token_response = mfa_service.create_mfa_token(db, account.id)

    return jsonify(token_response), 200

@auth_bp.route('/mfa/validate', methods=['POST'])
def validate_mfa_token():
    db = next(get_db())
    data = request.get_json()

    account_id = data.get('account_id')
    token = data.get('token')

    mfa_service = MFAService(MFARepository(db))

    try:
        result = mfa_service.validate_mfa_token(db, account_id, token)
        status_code = 200 if result['success'] else 401
        return jsonify(result), status_code
    except SQLAlchemyError as e:
        return jsonify({"error": "Unable to process your request"}), 500