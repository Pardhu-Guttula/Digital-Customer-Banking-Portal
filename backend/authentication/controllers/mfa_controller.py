# Epic Title: Login and Authentication

from flask import Blueprint, request, jsonify
from sqlalchemy.exc import SQLAlchemyError
from backend.database.config import get_db
from backend.authentication.repositories.mfa_repository import MFARepository
from backend.authentication.services.mfa_service import MFAService

mfa_bp = Blueprint('mfa', __name__)

@mfa_bp.route('/mfa/setup', methods=['POST'])
def setup_mfa():
    db = next(get_db())
    data = request.get_json()

    account_id = data.get('account_id')
    mfa_method = data.get('mfa_method')

    mfa_repository = MFARepository(db)
    mfa_service = MFAService(mfa_repository)

    try:
        result = mfa_service.setup_mfa(db, account_id, mfa_method)
        return jsonify(result), 201
    except SQLAlchemyError as e:
        return jsonify({"error": "Unable to process your request"}), 500

@mfa_bp.route('/mfa/activate', methods=['POST'])
def activate_mfa():
    db = next(get_db())
    data = request.get_json()

    account_id = data.get('account_id')
    mfa_method = data.get('mfa_method')

    mfa_repository = MFARepository(db)
    mfa_service = MFAService(mfa_repository)

    try:
        result = mfa_service.activate_mfa(db, account_id, mfa_method)
        return jsonify(result), 201
    except SQLAlchemyError as e:
        return jsonify({"error": "Unable to process your request"}), 500

@mfa_bp.route('/mfa/validate', methods=['POST'])
def validate_mfa_token():
    db = next(get_db())
    data = request.get_json()

    account_id = data.get('account_id')
    token = data.get('token')

    mfa_repository = MFARepository(db)
    mfa_service = MFAService(mfa_repository)

    try:
        result = mfa_service.validate_mfa_token(db, account_id, token)
        status_code = 200 if result['success'] else 401
        return jsonify(result), status_code
    except SQLAlchemyError as e:
        return jsonify({"error": "Unable to process your request"}), 500
