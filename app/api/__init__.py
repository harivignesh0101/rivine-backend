from fastapi import APIRouter

# Import routers from different API versions
from app.api.v1 import contact as contact_v1

# Create a main API router
router = APIRouter()

# Include v1 routers
router.include_router(contact_v1.router, prefix="/v1", tags=["v1-contact"])
