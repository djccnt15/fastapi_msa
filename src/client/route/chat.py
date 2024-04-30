from fastapi import APIRouter

from ..domain import chat_controller
from .enums import RouterTagEnum

router = APIRouter(prefix="/chat")

router.include_router(
    router=chat_controller.router,
    tags=[RouterTagEnum.CHAT],
)
