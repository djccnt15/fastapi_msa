from redis.asyncio.client import Redis


async def request_ping(
    *,
    redis: Redis,
) -> bool:
    res = bool(await redis.ping())
    return res
