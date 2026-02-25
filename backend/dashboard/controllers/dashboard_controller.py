# Epic Title: Personalized User Dashboard for Banking Products and Services

from flask import Blueprint, jsonify, request
from backend.dashboard.services.dashboard_service import DashboardService
import logging

dashboard_controller = Blueprint('dashboard_controller', __name__)
dashboard_service = DashboardService()

logging.basicConfig(level=logging.INFO)
logger = logging.getLogger(__name__)

@dashboard_controller.route('/dashboard', methods=['GET'])
def get_dashboard():
    user_id = request.args.get('user_id')
    if not user_id:
        logger.error("User ID not provided in request.")
        return jsonify({'error': 'User ID is required'}), 400
    
    try:
        logger.info(f"Fetching dashboard for user {user_id}")
        data = dashboard_service.get_personalized_dashboard(user_id)
        return jsonify(data), 200
    except Exception as e:
        logger.error(f"Error fetching dashboard: {e}")
        return jsonify({'error': 'Internal server error'}), 500