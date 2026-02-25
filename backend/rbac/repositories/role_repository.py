# Epic Title: Implement Role-Based Access Controls for User Authorization

import psycopg2
import logging

class RoleRepository:
    def __init__(self):
        self.connection = psycopg2.connect(
            host='localhost', database='service_db', user='service_user', password='service_password'
        )

    def get_user_role(self, user_id: int) -> dict:
        logger = logging.getLogger(__name__)
        cursor = self.connection.cursor()
        try:
            cursor.execute("SELECT role_id FROM user_roles WHERE user_id = %s", (user_id,))
            result = cursor.fetchone()
            if result:
                return {"user_id": user_id, "role_id": result[0]}
            return None
        except psycopg2.Error as e:
            logger.error(f"Error fetching user role: {e}")
            raise
        finally:
            cursor.close()

    def get_role_permissions(self, role_id: int) -> list:
        logger = logging.getLogger(__name__)
        cursor = self.connection.cursor()
        try:
            cursor.execute(
                "SELECT p.permission_name FROM roles_permissions rp "
                "JOIN permissions p ON rp.permission_id = p.permission_id "
                "WHERE rp.role_id = %s", (role_id,)
            )
            result = cursor.fetchall()
            return [row[0] for row in result]
        except psycopg2.Error as e:
            logger.error(f"Error fetching role permissions: {e}")
            raise
        finally:
            cursor.close()