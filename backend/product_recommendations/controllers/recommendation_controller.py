# Epic Title: Implement Product Recommendations Based on User Preferences

from flask import Blueprint, request, jsonify
from backend.product_recommendations.services.recommendation_service import generate_recommendations

recommendation_bp = Blueprint('recommendation', __name__)

@recommendation_bp.route('/generate/<int:user_id>', methods=['POST'])
def generate(user_id):
    try:
        recommendations = generate_recommendations(user_id)
        return jsonify(recommendations), 200
    except Exception as e:
        return jsonify({"error": str(e)}), 500