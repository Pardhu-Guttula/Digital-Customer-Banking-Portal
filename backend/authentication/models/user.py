# Epic Title: Secure and Efficient Data Storage with PostgreSQL

from typing import Optional
from werkzeug.security import check_password_hash
from backend.database.schemas.user_schema import UserSchema

class User:
    def __init__(self, id: int, email: str, password_hash: str):
        self.id = id
        self.email = email
        self.password_hash = password_hash

    def verify_password(self, password: str) -> bool:
        return check_password_hash(self.password_hash, password)

class UserRepository:
    def find_by_email(self, email: str) -> Optional[User]:
        user_data = UserSchema.get_user_by_email(email)
        if user_data:
            return User(**user_data)
        return None