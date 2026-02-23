# Epic Title: Update Product Quantity in Shopping Cart

import logging
from flask import Flask
from backend.shopping_cart.controllers.cart_controller import cart_bp
from backend.product_listings.controllers.product_controller import product_bp
from backend.authentication.controllers.login_controller import login_bp
from backend.authentication.controllers.register_controller import register_bp
from backend.authentication.controllers.password_recovery_controller import password_recovery_bp

def create_app() -> Flask:
    app = Flask(__name__)
    app.register_blueprint(cart_bp)
    app.register_blueprint(product_bp)
    app.register_blueprint(login_bp)
    app.register_blueprint(register_bp)
    app.register_blueprint(password_recovery_bp)
    logging.basicConfig(level=logging.INFO)
    return app

if __name__ == '__main__':
    app = create_app()
    app.run(host='0.0.0.0', port=5000, debug=True)