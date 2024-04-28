from fastapi import APIRouter, Depends, HTTPException
from redis import exceptions as redis_exception
from redis.client import Redis
from starlette import status

from src.server.db import redis_db

from ..business import redis_process
from ..model import ping

router = APIRouter(prefix="/redis")


@router.get("/ping")
async def check_ping(
    redis: Redis = Depends(redis_db.get_redis),
) -> ping.PongModel:
    try:
        response = await redis_process.request_ping(redis=redis)
    except redis_exception.ConnectionError:
        raise HTTPException(
            status_code=status.HTTP_500_INTERNAL_SERVER_ERROR,
            detail="Redis Server Not Answers",
        )
    return ping.PongModel(
        pong=response,
    )
