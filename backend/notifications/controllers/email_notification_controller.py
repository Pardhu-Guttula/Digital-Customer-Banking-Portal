# Epic Title: Email notifications for status updates

from flask import Blueprint, request, jsonify
from backend.notifications.services.email_service import EmailService
from backend.database.config import get_db

email_notification_bp = Blueprint('email_notification', __name__)

@email_notification_bp.route('/notify/status-change', methods=['POST'])
def notify_status_change():
    db = next(get_db())
    data = request.get_json()

    email_service = EmailService(db)
    
    try:
        email_service.send_status_update(data)
        return jsonify({"message": "Email notification sent successfully"}), 200
    except Exception as e:
        return jsonify({"error": str(e)}), 500