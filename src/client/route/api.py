from fastapi import APIRouter

from ..domain import server_controller
from .enums import RouterTagEnum

router = APIRouter(prefix="/api")

router.include_router(
    router=server_controller.router,
    tags=[RouterTagEnum.SERVER],
)
