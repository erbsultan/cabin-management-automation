from fastapi import FastAPI

from app.config import settings

app = FastAPI(
    title=settings.app_name,
    version="0.1.0",
)


@app.get("/")
def root():
    return {
        "message": "Cabin Management System API",
        "status": "running",
    }


@app.get("/health")
def health_check():
    return {
        "status": "ok",
        "service": settings.app_name,
        "environment": settings.app_env,
    }
