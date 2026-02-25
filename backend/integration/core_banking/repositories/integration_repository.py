# Epic Title: Integrate Self-Service Portal with Core Banking System

import psycopg2
import requests
import logging

class IntegrationRepository:
    def __init__(self):
        self.local_db_conn = psycopg2.connect(
            host='localhost', database='service_db', user='service_user', password='service_password'
        )
        self.external_api_url = 'http://corebanking.example/api/data'

    def get_local_data(self) -> list:
        cursor = self.local_db_conn.cursor()
        try:
            cursor.execute("SELECT id, data FROM local_table")
            data = cursor.fetchall()
            return data
        except psycopg2.Error as e:
            logging.error(f"Error fetching local data: {e}")
            raise
        finally:
            cursor.close()

    def get_external_data(self) -> list:
        try:
            response = requests.get(self.external_api_url)
            response.raise_for_status()
            return response.json()
        except requests.RequestException as e:
            logging.error(f"Error fetching external data: {e}")
            raise

    def update_local_system(self, data: dict):
        cursor = self.local_db_conn.cursor()
        try:
            cursor.execute("INSERT INTO local_table (id, data) VALUES (%s, %s)", (data['id'], data['data']))
            self.local_db_conn.commit()
        except psycopg2.Error as e:
            self.local_db_conn.rollback()
            logging.error(f"Error updating local system: {e}")
            raise
        finally:
            cursor.close()

    def update_external_system(self, data: dict):
        try:
            response = requests.post(self.external_api_url, json=data)
            response.raise_for_status()
        except requests.RequestException as e:
            logging.error(f"Error updating external system: {e}")
            raise