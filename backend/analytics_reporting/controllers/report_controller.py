# Epic Title: Track and Analyze Sales Data

from flask import Blueprint, jsonify
from backend.analytics_reporting.services.analytics_service import generate_analytics_report

report_bp = Blueprint('report', __name__)

@report_bp.route('/generate', methods=['GET'])
def generate_report():
    try:
        report = generate_analytics_report()
        return jsonify(report), 200
    except Exception as e:
        return jsonify({"error": str(e)}), 500