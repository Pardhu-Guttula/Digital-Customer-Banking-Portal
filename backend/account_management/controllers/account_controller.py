# Epic Title: Develop streamlined workflows for submitting account opening requests

from flask import Blueprint, request, jsonify
from sqlalchemy.exc import SQLAlchemyError
from backend.database.config import get_db
from backend.account_management.services.account_service import AccountService

account_bp = Blueprint('account', __name__)

@account_bp.route('/account/open', methods=['POST'])
def open_account():
    db = next(get_db())
    data = request.get_json()

    account_service = AccountService(db)
    
    try:
        result = account_service.process_opening_request(data)
        if not result['success']:
            return jsonify({"error": result['message']}), 400
        return jsonify({"message": "Account opening request successfully submitted"}), 200
    except SQLAlchemyError as e:
        return jsonify({"error": "Backend processing error"}), 500