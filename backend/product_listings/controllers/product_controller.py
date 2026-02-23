# Epic Title: Develop Product Listing Page

from flask import Blueprint, request, jsonify
from pydantic import ValidationError
from backend.product_listings.models.product import Product
from backend.product_listings.services.product_service import ProductService

product_bp = Blueprint('product', __name__)

@product_bp.route('/add-product', methods=['POST'])
def add_product():
    try:
        product_data = request.json
        product = Product(**product_data)
        ProductService.add_product(product)
        return jsonify({"message": "Product successfully added"}), 201
    except ValidationError as e:
        return jsonify({"errors": e.errors()}), 400