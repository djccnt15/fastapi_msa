from ..config import rd as redis


async def request_ping():
    res = bool(redis.ping())
    return res
