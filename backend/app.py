# Epic Title: Implement Product Recommendations Based on User Preferences

from flask import Flask
from backend.product_recommendations.controllers.recommendation_controller import recommendation_bp

app = Flask(__name__)

app.register_blueprint(recommendation_bp, url_prefix='/api/recommendations')

@app.before_first_request
def startup():
    # Code to run on startup, e.g., establish db connection, initialize resources
    pass

@app.teardown_appcontext
def shutdown(exception):
    # Code to run on shutdown, e.g., close db connection, clean up resources
    pass

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000)