import aiohttp
from fastapi import APIRouter, HTTPException
from starlette import status

from ..business import process
from ..model import ping

router = APIRouter(prefix="/server")


@router.get("/ping")
async def check_ping() -> ping.PongModel:
    try:
        response = await process.ping_process()
    except aiohttp.ClientConnectionError:
        raise HTTPException(
            status_code=status.HTTP_500_INTERNAL_SERVER_ERROR,
            detail="Server Not Answers",
        )
    return response
