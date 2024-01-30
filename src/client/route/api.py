from fastapi import APIRouter

from ..domain import server
from .enums import Tags

router = APIRouter()

router.include_router(
    router=server.router,
    tags=[Tags.SERVER],
)
