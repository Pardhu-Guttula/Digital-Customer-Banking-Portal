# Epic Title: Develop streamlined workflows for submitting service modification requests

from flask import Blueprint, request, jsonify
from sqlalchemy.exc import SQLAlchemyError
from backend.database.config import get_db
from backend.account_management.services.service_modification_service import ServiceModificationService

service_modification_bp = Blueprint('service_modification', __name__)

@service_modification_bp.route('/service/modify', methods=['POST'])
def modify_service():
    db = next(get_db())
    data = request.get_json()

    service_modification_service = ServiceModificationService(db)
    
    try:
        result = service_modification_service.process_modification_request(data)
        if not result['success']:
            return jsonify({"error": result['message']}), 400
        return jsonify({"message": "Service modification request successfully submitted"}), 200
    except SQLAlchemyError as e:
        return jsonify({"error": "Backend processing error"}), 500