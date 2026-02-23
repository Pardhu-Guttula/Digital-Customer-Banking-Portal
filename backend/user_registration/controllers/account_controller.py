# Epic Title: User Registration Form

from flask import Blueprint, request, jsonify
from sqlalchemy.exc import SQLAlchemyError
from backend.database.config import get_db
from backend.user_registration.repositories.account_repository import AccountRepository
from backend.user_registration.services.account_service import AccountService

account_bp = Blueprint('account', __name__)

@account_bp.route('/register', methods=['POST'])
def register():
    db = next(get_db())
    data = request.get_json()

    name = data.get('name')
    email = data.get('email')
    password = data.get('password')

    account_repository = AccountRepository(db)
    account_service = AccountService(account_repository)

    try:
        result = account_service.create_account(db, name, email, password)
        if result['success']:
            account = result['account']
            return jsonify({
                "id": account.id,
                "name": account.name,
                "email": account.email
            }), 201
        return jsonify({"error": result.get("error")}), 400
    except SQLAlchemyError as e:
        return jsonify({"error": "Unable to process your request"}), 500