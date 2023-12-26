import aiohttp

from src.client import configs

from ..model import ping

config = configs.config.server


async def request_ping():
    async with aiohttp.ClientSession() as session:
        async with session.get(f"{config.host}:{config.port}/ping") as response:
            status = response.status
            body = await response.text()

    return ping.PongModel(
        status=status,
        body=body,
    )
