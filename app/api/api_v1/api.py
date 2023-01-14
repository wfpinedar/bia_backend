from fastapi import APIRouter

from app.api.api_v1.endpoints import meter

api_router = APIRouter()
api_router.include_router(meter.router, prefix="/meter", tags=["meter"])
