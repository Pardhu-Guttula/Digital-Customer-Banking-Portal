# Epic Title: Remove Product from Shopping Cart

from flask import Blueprint, request, jsonify
from pydantic import ValidationError
from backend.shopping_cart.models.cart import CartItem
from backend.shopping_cart.services.cart_service import CartService

cart_bp = Blueprint('cart', __name__)

@cart_bp.route('/remove-from-cart', methods=['DELETE'])
def remove_from_cart():
    try:
        cart_data = request.json
        cart_item = CartItem(**cart_data)
        result = CartService.remove_item_from_cart(cart_item)
        if result:
            return jsonify({"message": "Product removed from cart"}), 200
        else:
            return jsonify({"error": "Product not found in cart"}), 400
    except ValidationError as e:
        return jsonify({"errors": e.errors()}), 400