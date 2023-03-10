from fastapi import FastAPI
from .router.health_check import health_check

APP: FastAPI = FastAPI(
    title="HomeWork test echo"
)

APP.include_router(health_check, tags=["health_check"])
