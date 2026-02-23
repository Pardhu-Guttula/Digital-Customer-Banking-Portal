# Epic Title: Email notifications for status updates

from sqlalchemy.orm import Session

class EmailTemplateRepository:
    def __init__(self, db_session: Session):
        self.db_session = db_session

    def get_template(self, template_name: str) -> str:
        query = "SELECT content FROM email_templates WHERE name = :name"
        result = self.db_session.execute(query, {'name': template_name}).fetchone()
        return result['content'] if result else ""