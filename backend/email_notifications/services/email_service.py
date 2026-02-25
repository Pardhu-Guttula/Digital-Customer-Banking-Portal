# Epic Title: Log Email Communication in PostgreSQL

import smtplib
import logging
from email.mime.text import MIMEText
from backend.email_notifications.repositories.email_log_repository import EmailLogRepository

class EmailNotificationService:
    def __init__(self):
        self.repository = EmailLogRepository()
        self.smtp_server = 'smtp.example.com'
        self.smtp_port = 587
        self.sender_email = 'no-reply@example.com'
        self.sender_password = 'password'

    def send_email(self, request_id: int, status: str, user_email: str):
        logger = logging.getLogger(__name__)
        
        if self.repository.check_duplicate_email(request_id, status):
            logger.info(f"Duplicate email detected for request ID: {request_id} with status: {status}")
            return False
        
        subject = f"Status Update for Request ID {request_id}"
        body = f"The status of your request (ID: {request_id}) has been updated to: {status}"
        message = MIMEText(body)
        message['Subject'] = subject
        message['From'] = self.sender_email
        message['To'] = user_email
        
        try:
            with smtplib.SMTP(self.smtp_server, self.smtp_port) as server:
                server.starttls()
                server.login(self.sender_email, self.sender_password)
                server.sendmail(self.sender_email, user_email, message.as_string())
            logger.info(f"Email sent successfully to {user_email}")
            self.repository.log_email_sent(request_id, status, user_email, "sent")
            return True
        except Exception as e:
            logger.error(f"Failed to send email: {e}")
            self.repository.log_email_sent(request_id, status, user_email, "failed")
            return False