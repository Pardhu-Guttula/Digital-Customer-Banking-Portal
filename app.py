# Epic Title: Allow Users to View Order History

import logging
from flask import Flask
from backend.checkout.controllers.payment_controller import payment_bp
from backend.checkout.controllers.address_controller import address_bp
from backend.shopping_cart.controllers.cart_controller import cart_bp
from backend.authentication.controllers.login_controller import login_bp
from backend.authentication.controllers.register_controller import register_bp
from backend.authentication.controllers.password_recovery_controller import password_recovery_bp
from backend.order_management.controllers.order_controller import order_bp
from backend.order_management.controllers.order_history_controller import order_history_bp

def create_app() -> Flask:
    app = Flask(__name__)
    app.register_blueprint(payment_bp)
    app.register_blueprint(address_bp)
    app.register_blueprint(cart_bp)
    app.register_blueprint(login_bp)
    app.register_blueprint(register_bp)
    app.register_blueprint(password_recovery_bp)
    app.register_blueprint(order_bp)
    app.register_blueprint(order_history_bp)
    logging.basicConfig(level=logging.INFO)
    return app

if __name__ == '__main__':
    app = create_app()
    app.run(host='0.0.0.0', port=5000, debug=True)