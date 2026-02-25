# Epic Title: Personalized User Dashboard for Banking Products and Services

import psycopg2
import logging

logger = logging.getLogger(__name__)

class DashboardRepository:
    def fetch_user_dashboard(self, user_id: int) -> dict:
        connection = psycopg2.connect(
            host='localhost', database='bank_system', user='bank_user', password='bank_password'
        )
        cursor = connection.cursor()

        try:
            cursor.execute("""
                SELECT products, services 
                FROM user_dashboard 
                WHERE user_id = %s
            """, (user_id,))
            result = cursor.fetchone()
            if result:
                return {'products': result[0], 'services': result[1]}
        except psycopg2.Error as e:
            logger.error(f"Error fetching dashboard data: {e}")
        finally:
            cursor.close()
            connection.close()
        return {'products': [], 'services': []}