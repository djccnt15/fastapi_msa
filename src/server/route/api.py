from fastapi import APIRouter

from ..domain.notice.endpoint import notice_controller
from ..domain.redis.endpoint import redis_controller
from .enums.tag import RouterTagEnum

router = APIRouter(prefix="/api")

router.include_router(
    router=redis_controller.router,
    tags=[RouterTagEnum.REDIS],
)

router.include_router(
    router=notice_controller.router,
    tags=[RouterTagEnum.NOTICE],
)
