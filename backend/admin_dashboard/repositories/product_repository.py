# Epic Title: Personalized User Dashboard in React

import psycopg2
import logging

class ProductRepository:
    def __init__(self):
        self.connection = psycopg2.connect(
            host='localhost', database='service_db', user='service_user', password='service_password'
        )

    def get_products_for_user(self, user_profile: dict) -> list:
        logger = logging.getLogger(__name__)
        cursor = self.connection.cursor()
        eligible_products = []
        try:
            cursor.execute("SELECT product_id, product_name, eligibility_criteria FROM products")
            products = cursor.fetchall()
            for product in products:
                if self.check_eligibility(user_profile, product[2]):
                    eligible_products.append({
                        "product_id": product[0],
                        "product_name": product[1]
                    })
            return eligible_products
        except psycopg2.Error as e:
            logger.error(f"Error fetching products: {e}")
            raise
        finally:
            cursor.close()

    def check_eligibility(self, user_profile: dict, eligibility_criteria: str) -> bool:
        # Implement eligibility check logic
        return user_profile["eligibility"] == eligibility_criteria