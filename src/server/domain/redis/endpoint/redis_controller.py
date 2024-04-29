from fastapi import APIRouter, Depends
from redis.asyncio.client import Redis

from src.server.db import redis_db

from ..business import redis_process
from ..model import ping

router = APIRouter(prefix="/redis")


@router.get("/ping")
async def check_ping(
    redis: Redis = Depends(redis_db.get_redis),
) -> ping.PongModel:
    response = await redis_process.request_ping(redis=redis)
    return ping.PongModel(pong=response)
