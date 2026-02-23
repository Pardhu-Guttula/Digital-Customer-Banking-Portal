# Epic Title: Managing user roles and permissions

from flask import Flask, send_from_directory
from backend.access_control.controllers.role_controller import role_bp
from backend.access_control.controllers.permission_controller import permission_bp
from backend.access_control.controllers.user_controller import user_bp
from backend.database.config import Base, engine
import os
from cryptography.fernet import Fernet

app = Flask(__name__)

encryption_key_file = 'encryption_key'
if not os.path.exists(encryption_key_file):
    key = Fernet.generate_key().decode()
    with open(encryption_key_file, 'w') as file:
        file.write(key)

with open(encryption_key_file, 'r') as file:
    os.environ['ENCRYPTION_KEY'] = file.read()

app.register_blueprint(role_bp, url_prefix='/api')
app.register_blueprint(permission_bp, url_prefix='/api')
app.register_blueprint(user_bp, url_prefix='/api')

@app.before_first_request
def startup():
    Base.metadata.create_all(bind=engine)

@app.teardown_appcontext
def shutdown(exception):
    pass

@app.route('/')
def serve():
    return send_from_directory(app.static_folder, 'index.html')

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000)