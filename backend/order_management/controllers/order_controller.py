# Epic Title: Track User Orders

from flask import Blueprint, request, jsonify
from pydantic import ValidationError
from backend.order_management.models.order import Order, OrderStatus
from backend.order_management.services.order_service import OrderService

order_bp = Blueprint('order', __name__)

@order_bp.route('/view-orders/<int:user_id>', methods=['GET'])
def view_orders(user_id: int):
    try:
        orders = OrderService.get_orders_by_user_id(user_id)
        return jsonify(orders), 200
    except Exception as e:
        return jsonify({"error": f"Error retrieving orders: {str(e)}"}), 500

@order_bp.route('/update-order-status/<int:order_id>', methods=['PUT'])
def update_order_status(order_id: int):
    try:
        status_data = request.json
        status = OrderStatus(**status_data)
        result = OrderService.update_order_status(order_id, status)
        if result:
            return jsonify({"message": "Order status updated successfully"}), 200
        else:
            return jsonify({"error": "Error updating order status"}), 500
    except ValidationError as e:
        return jsonify({"errors": e.errors()}), 400

@order_bp.route('/filter-orders/<int:user_id>', methods=['GET'])
def filter_orders(user_id: int):
    status = request.args.get('status')
    try:
        orders = OrderService.filter_orders_by_status(user_id, status)
        return jsonify(orders), 200
    except Exception as e:
        return jsonify({"error": f"Error filtering orders: {str(e)}"}), 500