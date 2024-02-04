from fastapi import APIRouter

from ..domain import server_controller
from .enums import Tags

router = APIRouter()

router.include_router(
    router=server_controller.router,
    tags=[Tags.SERVER],
)
