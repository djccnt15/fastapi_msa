from ..service import redis_logic


async def request_ping():
    pong = await redis_logic.request_ping()
    return pong
