# Epic Title: Dashboard Backend Data Integration

from flask import Blueprint, request, jsonify
from sqlalchemy.exc import SQLAlchemyError
from backend.database.config import get_db
from backend.dashboard.services.dashboard_service import DashboardService

dashboard_bp = Blueprint('dashboard', __name__)

@dashboard_bp.route('/dashboard', methods=['GET'])
def get_dashboard():
    db = next(get_db())
    user_id = request.args.get('user_id')

    dashboard_service = DashboardService(db)

    try:
        dashboard_data = dashboard_service.fetch_dashboard_data(user_id)
        if dashboard_data is None:
            return jsonify({"error": "User profile data missing"}), 404
        return jsonify(dashboard_data), 200
    except SQLAlchemyError as e:
        return jsonify({"error": "Unable to process your request"}), 500