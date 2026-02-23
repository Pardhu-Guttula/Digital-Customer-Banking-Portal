# Epic Title: User Registration

import logging
from flask import Flask
from backend.authentication.controllers.register_controller import register_bp

def create_app() -> Flask:
    app = Flask(__name__)
    app.register_blueprint(register_bp)
    logging.basicConfig(level=logging.INFO)
    return app

if __name__ == '__main__':
    app = create_app()
    app.run(host='0.0.0.0', port=5000, debug=True)