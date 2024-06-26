from fastapi import APIRouter

from ..domain.default.endpoint import default_controller
from .enums.tag import RouterTagEnum

router = APIRouter()

router.include_router(
    router=default_controller.router,
    tags=[RouterTagEnum.DEFAULT],
)
