# Epic Title: Edit Product Details

from flask import Blueprint, request, jsonify
from pydantic import ValidationError
from backend.product_listings.models.product import Product
from backend.product_listings.services.product_service import ProductService

product_bp = Blueprint('product', __name__)

@product_bp.route('/edit-product', methods=['PUT'])
def edit_product():
    try:
        product_data = request.json
        product = Product(**product_data)
        success = ProductService.update_product_details(product)
        if success:
            return jsonify({"message": "Product details successfully updated"}), 200
        else:
            return jsonify({"error": "Product not found"}), 404
    except ValidationError as e:
        return jsonify({"errors": e.errors()}), 400