from redis.client import Redis


async def request_ping(
    *,
    redis: Redis,
) -> bool:
    res = bool(redis.ping())
    return res
