from redis.client import Redis


async def request_ping(
    *,
    redis: Redis,
):
    res = bool(redis.ping())
    return res
