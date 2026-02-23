# Epic Title: Data Storage and Retrieval Using PostgreSQL

from flask import Flask
from backend.analytics_reporting.controllers.report_controller import report_bp
from backend.analytics_reporting.controllers.insight_controller import insight_bp
from backend.database.config import Base, engine

app = Flask(__name__)

# Register blueprints
app.register_blueprint(report_bp, url_prefix='/api/reports')
app.register_blueprint(insight_bp, url_prefix='/api/insights')

@app.before_first_request
def startup():
    # Create all tables in the database
    Base.metadata.create_all(bind=engine)

@app.teardown_appcontext
def shutdown(exception):
    # Code to run on shutdown, e.g., close db connection, clean up resources
    pass

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000)