from redis.client import Redis

from ..service import redis_logic


async def request_ping(
    *,
    redis: Redis,
):
    pong = await redis_logic.request_ping(redis=redis)
    return pong
