# Epic Title: Document Upload

from sqlalchemy.orm import Session

class DocumentRepository:
    def __init__(self, db_session: Session):
        self.db_session = db_session

    def save_document(self, data: dict):
        query = """
            INSERT INTO documents (filename, path)
            VALUES (:filename, :path)
        """
        self.db_session.execute(query, data)
        self.db_session.commit()