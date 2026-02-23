# Epic Title: Allow Users to View Order History

from flask import Blueprint, request, jsonify
from pydantic import ValidationError
from backend.order_management.services.order_history_service import OrderHistoryService

order_history_bp = Blueprint('order_history', __name__)

@order_history_bp.route('/order-history/<int:user_id>', methods=['GET'])
def view_order_history(user_id: int):
    try:
        sort_by_date = request.args.get('sort_by_date', default='false').lower() == 'true'
        history = OrderHistoryService.get_order_history(user_id, sort_by_date)
        return jsonify(history), 200
    except Exception as e:
        return jsonify({"error": f"Error retrieving order history: {str(e)}"}), 500