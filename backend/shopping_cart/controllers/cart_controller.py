# Epic Title: Persist Shopping Cart Data in PostgreSQL

from flask import Blueprint, request, jsonify
from pydantic import ValidationError
from backend.shopping_cart.models.cart import CartItem, Cart
from backend.shopping_cart.services.cart_service import CartService

cart_bp = Blueprint('cart', __name__)

@cart_bp.route('/update-cart', methods=['PUT'])
def update_cart():
    try:
        cart_data = request.json
        cart = Cart(**cart_data)
        result = CartService.update_cart(cart)
        if result:
            return jsonify({"message": "Cart updated successfully"}), 200
        else:
            return jsonify({"error": "Error updating cart"}), 500
    except ValidationError as e:
        return jsonify({"errors": e.errors()}), 400

@cart_bp.route('/get-cart/<int:user_id>', methods=['GET'])
def get_cart(user_id: int):
    try:
        cart = CartService.get_cart_by_user_id(user_id)
        return jsonify(cart), 200
    except Exception as e:
        return jsonify({"error": f"Error retrieving cart: {str(e)"}), 500