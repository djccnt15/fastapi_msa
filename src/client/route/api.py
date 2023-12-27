from fastapi import APIRouter

from ..domain import redis, server
from .enums import Tags

router = APIRouter()

router.include_router(
    router=server.router,
    tags=[Tags.SERVER],
)

router.include_router(
    router=redis.router,
    tags=[Tags.REDIS],
)
