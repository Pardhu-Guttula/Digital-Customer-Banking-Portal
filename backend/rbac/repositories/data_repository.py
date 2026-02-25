# Epic Title: Secure Role-Based Data Segregation in PostgreSQL

import psycopg2
import logging
from cryptography.fernet import Fernet

class DataRepository:
    def __init__(self):
        self.connection = psycopg2.connect(
            host='localhost', database='service_db', user='service_user', password='service_password'
        )
        self.encryption_key = Fernet.generate_key()
        self.fernet = Fernet(self.encryption_key)
    
    def get_data_for_role(self, role: str) -> list:
        logger = logging.getLogger(__name__)
        cursor = self.connection.cursor()
        try:
            cursor.execute("SELECT data FROM data_table WHERE role = %s", (role,))
            data_encrypted = cursor.fetchall()
            data_decrypted = [self.fernet.decrypt(row[0]) for row in data_encrypted]
            return data_decrypted
        except psycopg2.Error as e:
            logger.error(f"Error fetching data for role {role}: {e}")
            raise
        finally:
            cursor.close()

    def insert_data(self, data: str, role: str):
        logger = logging.getLogger(__name__)
        cursor = self.connection.cursor()
        try:
            data_encrypted = self.fernet.encrypt(data.encode())
            cursor.execute("INSERT INTO data_table (data, role) VALUES (%s, %s)", (data_encrypted, role))
            self.connection.commit()
        except psycopg2.Error as e:
            self.connection.rollback()
            logger.error(f"Error inserting data for role {role}: {e}")
            raise
        finally:
            cursor.close()