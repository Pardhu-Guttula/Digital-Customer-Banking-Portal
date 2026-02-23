# Epic Title: Track and Analyze User Behavior

from flask import Blueprint, jsonify
from backend.analytics_reporting.services.behavior_insight_service import generate_behavior_insights

insight_bp = Blueprint('insight', __name__)

@insight_bp.route('/generate', methods=['GET'])
def generate_insight():
    try:
        insights = generate_behavior_insights()
        return jsonify(insights), 200
    except Exception as e:
        return jsonify({"error": str(e)}), 500