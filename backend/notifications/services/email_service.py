# Epic Title: Email notifications for status updates

import smtplib
from email.mime.text import MIMEText
from backend.notifications.repositories.email_template_repository import EmailTemplateRepository

class EmailService:
    def __init__(self, db):
        self.email_template_repository = EmailTemplateRepository(db)

    def send_status_update(self, data: dict):
        user_email = data['email']
        status = data['status']

        template = self.email_template_repository.get_template('status_update')
        content = template.format(status=status)
        
        message = MIMEText(content)
        message['Subject'] = "Request Status Update"
        message['From'] = "no-reply@example.com"
        message['To'] = user_email

        with smtplib.SMTP('smtp.example.com') as server:
            server.starttls()
            server.login("username", "password")
            server.sendmail(message['From'], [message['To']], message.as_string())