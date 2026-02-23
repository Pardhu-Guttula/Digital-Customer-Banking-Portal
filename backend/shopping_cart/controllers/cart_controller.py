# Epic Title: Update Product Quantity in Shopping Cart

from flask import Blueprint, request, jsonify
from pydantic import ValidationError
from backend.shopping_cart.models.cart import CartItem
from backend.shopping_cart.services.cart_service import CartService

cart_bp = Blueprint('cart', __name__)

@cart_bp.route('/update-cart-item', methods=['PUT'])
def update_cart_item():
    try:
        cart_data = request.json
        cart_item = CartItem(**cart_data)
        result = CartService.update_cart_item(cart_item)
        if result:
            return jsonify({"message": "Cart item updated successfully"}), 200
        else:
            return jsonify({"error": "Quantity exceeds available stock"}), 400
    except ValidationError as e:
        return jsonify({"errors": e.errors()}), 400