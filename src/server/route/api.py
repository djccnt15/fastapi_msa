from fastapi import APIRouter

from ..domain import redis_controller
from .enums import tag

router = APIRouter(prefix="/api")

router.include_router(
    router=redis_controller.router,
    tags=[tag.RouterTagEnum.REDIS],
)
