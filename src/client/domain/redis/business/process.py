from ..service import logic


async def ping_process():
    pong = await logic.request_ping()
    return pong
