# Epic Title: Order Confirmation Display After Successful Purchase

from flask import Blueprint, request, jsonify
from pydantic import ValidationError
from backend.order_management.models.order import Order
from backend.order_management.services.confirmation_service import ConfirmationService

confirmation_bp = Blueprint('confirmation', __name__)

@confirmation_bp.route('/order-confirmation/<int:order_id>', methods=['GET'])
def order_confirmation(order_id: int):
    try:
        confirmation = ConfirmationService.get_order_confirmation(order_id)
        return jsonify(confirmation), 200
    except Exception as e:
        return jsonify({"error": f"Error retrieving order confirmation: {str(e)}"}), 500