# Epic Title: Enable Users to Leave Reviews and Ratings for Products

from flask import Blueprint, request, jsonify
from backend.reviews_ratings.services.review_service import submit_review

review_bp = Blueprint('review', __name__)

@review_bp.route('/submit', methods=['POST'])
def submit():
    data = request.get_json()
    content = data.get('content')
    rating = data.get('rating')
    product_id = data.get('product_id')
    user_id = data.get('user_id')

    if not rating:
        return jsonify({"error": "Rating is required"}), 400
    if len(content) > 500:
        return jsonify({"error": "Review content exceeds 500 characters"}), 400

    try:
        submit_review(content, rating, product_id, user_id)
        return jsonify({"message": "Review submitted successfully"}), 200
    except Exception as e:
        return jsonify({"error": str(e)}), 500