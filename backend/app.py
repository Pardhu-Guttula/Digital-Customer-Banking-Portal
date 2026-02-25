# Epic Title: Real-time Status Updates Using React and Redis

from flask import Flask
from flask_socketio import SocketIO
from backend.realtime_status_updates.controllers.status_update_controller import status_update_controller
import logging

app = Flask(__name__)
app.register_blueprint(status_update_controller, url_prefix='/api')

socketio = SocketIO(app, cors_allowed_origins="*")

logging.basicConfig(level=logging.INFO)
logger = logging.getLogger(__name__)

@app.route('/')
def home():
    return "Welcome to the Real-time Status Update System"

if __name__ == '__main__':
    logger.info("Starting the Real-time Status Update System...")
    socketio.run(app, debug=True)