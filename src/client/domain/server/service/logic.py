import aiohttp

from src.client import config

from ..model import ping

host = config.configs("server_host")
port = config.configs("server_port")


async def request_ping():
    async with aiohttp.ClientSession() as session:
        async with session.get(f"{host}:{port}/ping") as response:
            status = response.status
            body = await response.text()

    return ping.PongModel(
        status=status,
        body=body,
    )
