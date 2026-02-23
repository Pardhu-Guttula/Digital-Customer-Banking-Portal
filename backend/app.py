# Epic Title: Responsive Design for Mobile using React

from flask import Flask, send_from_directory
from backend.authentication.controllers.auth_controller import auth_bp
from backend.database.config import Base, engine
import os
from cryptography.fernet import Fernet

app = Flask(__name__, static_folder='../frontend/build', static_url_path='/')

# Generate encryption key if not already existing
encryption_key_file = 'encryption_key'
if not os.path.exists(encryption_key_file):
    key = Fernet.generate_key().decode()
    with open(encryption_key_file, 'w') as file:
        file.write(key)

# Load encryption key to environment variable
with open(encryption_key_file, 'r') as file:
    os.environ['ENCRYPTION_KEY'] = file.read()

# Register blueprints
app.register_blueprint(auth_bp, url_prefix='/api')

@app.before_first_request
def startup():
    # Create all tables in the database
    Base.metadata.create_all(bind=engine)

@app.teardown_appcontext
def shutdown(exception):
    pass

@app.route('/')
def serve():
    return send_from_directory(app.static_folder, 'index.html')

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000)