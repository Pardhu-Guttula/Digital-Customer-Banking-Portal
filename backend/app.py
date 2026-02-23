# Epic Title: Store User Data Securely

from flask import Flask
from backend.user_registration.controllers.account_controller import account_bp
from backend.database.config import Base, engine
import os
from cryptography.fernet import Fernet

app = Flask(__name__)

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
app.register_blueprint(account_bp, url_prefix='/api')

@app.before_first_request
def startup():
    # Create all tables in the database
    Base.metadata.create_all(bind=engine)

@app.teardown_appcontext
def shutdown(exception):
    pass

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000)