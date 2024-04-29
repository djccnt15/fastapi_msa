from fastapi import HTTPException
from redis import exceptions as redis_exception
from redis.asyncio.client import Redis
from starlette import status

from ..service import redis_logic


async def request_ping(
    *,
    redis: Redis,
) -> bool:
    try:
        pong = await redis_logic.request_ping(redis=redis)
    except redis_exception.ConnectionError:
        raise HTTPException(
            status_code=status.HTTP_500_INTERNAL_SERVER_ERROR,
            detail="Redis Server Not Answers",
        )
    return pong
