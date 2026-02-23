# Epic Title: Integrate PostgreSQL Database for Data Management in the Admin Dashboard

from fastapi import FastAPI
from backend.admin_dashboard.controllers.dashboard_controller import router as dashboard_router

app = FastAPI()

app.include_router(dashboard_router, prefix="/admin", tags=["Admin Dashboard"])

@app.on_event("startup")
def startup():
    # Code to run on startup, e.g., establish db connection, initialize resources
    pass

@app.on_event("shutdown")
def shutdown():
    # Code to run on shutdown, e.g., close db connection, clean up resources
    pass

if __name__ == "__main__":
    import uvicorn
    uvicorn.run(app, host="0.0.0.0", port=8000)