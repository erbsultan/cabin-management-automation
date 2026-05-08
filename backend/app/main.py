from fastapi import FastAPI, status
from fastapi.responses import JSONResponse

from app.api.cabins import router as cabins_router
from app.config import settings
from app.database import check_database_connection

app = FastAPI(
    title=settings.app_name,
    version="0.1.0",
)

app.include_router(cabins_router)


@app.get("/")
def root():
    return {
        "message": "Cabin Management System API",
        "status": "running",
    }


@app.get("/health")
def health_check():
    database_ok = check_database_connection()

    if not database_ok:
        return JSONResponse(
            status_code=status.HTTP_503_SERVICE_UNAVAILABLE,
            content={
                "status": "error",
                "service": settings.app_name,
                "environment": settings.app_env,
                "database": "unavailable",
            },
        )

    return {
        "status": "ok",
        "service": settings.app_name,
        "environment": settings.app_env,
        "database": "ok",
    }
