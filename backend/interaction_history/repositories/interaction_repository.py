# Epic Title: Store User Interaction Data in PostgreSQL

import psycopg2
import logging

class InteractionRepository:
    def __init__(self):
        self.connection = psycopg2.connect(
            host='localhost', database='service_db', user='service_user', password='service_password'
        )

    def store_interaction(self, data: dict):
        logger = logging.getLogger(__name__)
        cursor = self.connection.cursor()
        try:
            cursor.execute("""
                INSERT INTO user_interactions (user_id, interaction_type, interaction_data)
                VALUES (%s, %s, %s)
            """, (data['user_id'], data['interaction_type'], data.get('interaction_data', {})))
            self.connection.commit()
            logger.info("Interaction data stored in PostgreSQL")
        except psycopg2.Error as e:
            self.connection.rollback()
            logger.error(f"Error storing interaction data: {e}")
            raise
        finally:
            cursor.close()

    def retrieve_interactions_by_user(self, user_id: int):
        logger = logging.getLogger(__name__)
        cursor = self.connection.cursor()
        try:
            cursor.execute("""
                SELECT user_id, interaction_type, interaction_data
                FROM user_interactions
                WHERE user_id = %s
            """, (user_id,))
            rows = cursor.fetchall()
            return [{"user_id": row[0], "interaction_type": row[1], "interaction_data": row[2]} for row in rows]
        except psycopg2.Error as e:
            self.connection.rollback()
            logger.error(f"Error retrieving interactions: {e}")
            raise
        finally:
            cursor.close()