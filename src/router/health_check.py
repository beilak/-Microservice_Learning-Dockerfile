"""Target and Target Cneter Router"""

from fastapi import APIRouter, status

health_check: APIRouter = APIRouter()


@health_check.get(
    "/health/",
    status_code=status.HTTP_200_OK,
)
async def health() -> dict:
    return {"status": "OK"}
