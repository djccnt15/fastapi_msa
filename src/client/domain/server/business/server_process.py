from ..service import server_logic


async def request_ping():
    pong = await server_logic.request_ping()
    return pong
