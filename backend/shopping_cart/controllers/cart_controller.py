# Epic Title: Add Product to Shopping Cart

from flask import Blueprint, request, jsonify
from pydantic import ValidationError
from backend.shopping_cart.models.cart import Cart, CartItem
from backend.shopping_cart.services.cart_service import CartService

cart_bp = Blueprint('cart', __name__)

@cart_bp.route('/add-to-cart', methods=['POST'])
def add_to_cart():
    try:
        cart_data = request.json
        cart_item = CartItem(**cart_data)
        result = CartService.add_item_to_cart(cart_item)
        if result:
            return jsonify({"message": "Product added to cart"}), 200
        else:
            return jsonify({"error": "Product not in stock"}), 400
    except ValidationError as e:
        return jsonify({"errors": e.errors()}), 400