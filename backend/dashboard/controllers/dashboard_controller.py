# Epic Title: Personalized Dashboard Layout

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
        dashboard_layout = dashboard_service.get_user_dashboard(user_id)
        if dashboard_layout is None:
            return jsonify({"error": "User profile data missing"}), 404
        return jsonify(dashboard_layout), 200
    except SQLAlchemyError as e:
        return jsonify({"error": "Unable to process your request"}), 500