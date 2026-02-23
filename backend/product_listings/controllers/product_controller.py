# Epic Title: Product Listing Page

from flask import Blueprint, request, jsonify
import logging
from backend.product_listings.services.product_service import ProductService

product_bp = Blueprint('product', __name__)
logger = logging.getLogger(__name__)

@product_bp.route('/products', methods=['GET'])
def get_products():
    try:
        page = int(request.args.get('page', 1))
        per_page = int(request.args.get('per_page', 10))
        products = ProductService.get_all_products(page, per_page)
        return jsonify(products), 200
    except Exception as e:
        logger.error(f"Error retrieving products: {e}")
        return jsonify({"error": "Could not retrieve products"}), 500