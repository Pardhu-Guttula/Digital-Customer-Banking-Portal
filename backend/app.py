# Epic Title: Integrate with PostgreSQL for Data Storage

from fastapi import FastAPI
from backend.order_management.controllers.order_controller import router as order_router

app = FastAPI()

app.include_router(order_router, prefix="/orders", tags=["orders"])

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