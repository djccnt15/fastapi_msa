from fastapi import APIRouter, HTTPException
from redis import exceptions as redis_exception
from starlette import status

from ..business import redis_process
from ..model import ping

router = APIRouter(prefix="/redis")


@router.get("/ping")
async def check_ping() -> ping.PongModel:
    try:
        response = await redis_process.request_ping()
    except redis_exception.ConnectionError:
        raise HTTPException(
            status_code=status.HTTP_500_INTERNAL_SERVER_ERROR,
            detail="Redis Server Not Answers",
        )
    return ping.PongModel(
        pong=response,
    )
