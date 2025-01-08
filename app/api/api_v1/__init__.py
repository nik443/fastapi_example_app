from fastapi import APIRouter

from app.core.config import settings

from app.api.api_v1.users import router as users_router


router = APIRouter(
    prefix=settings.api.v1.prefix,
)

router.include_router(
    users_router,
    prefix=settings.api.v1.users,
)
