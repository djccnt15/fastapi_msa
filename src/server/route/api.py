from fastapi import APIRouter

from ..domain import notice_controller, redis_controller
from .enums import tag

router = APIRouter(prefix="/api")

router.include_router(
    router=redis_controller.router,
    tags=[tag.RouterTagEnum.REDIS],
)

router.include_router(
    router=notice_controller.router,
    tags=[tag.RouterTagEnum.NOTICE],
)
