from typing import Any, Awaitable

from redis.client import Redis
from sqlalchemy.ext.asyncio import AsyncSession

from src.server.common.exception import exceptions
from src.server.db import redis_db

from ..converter import notice_converter
from ..model import notice_model, redis_model
from ..service import notice_logic

REDIS_NOTICE_KEY = "notice:%s"


async def create_notice(
    *,
    db: AsyncSession,
    data: notice_model.NoticeCreateRequest,
) -> None:
    notice = await notice_logic.find_notice_by_title(db=db, data=data)
    if notice:
        raise exceptions.NotUniqueException(obj="title", detail=data.title)
    await notice_logic.create_notice(db=db, data=data)


async def get_notice_list(
    *,
    db: AsyncSession,
    keyword: str,
    page: int,
    size: int,
) -> notice_model.NoticeListResponse:
    total = await notice_logic.get_notice_count(db=db, keyword=keyword)
    if not total:
        raise exceptions.QueryResultEmpty
    notice_list = await notice_logic.get_notice_list(
        db=db, keyword=keyword, page=page, size=size
    )
    response_list = (
        notice_model.NoticeResponse.model_validate(obj=x) for x in notice_list
    )
    return notice_model.NoticeListResponse(
        total=total,
        notice_list=response_list,
    )


async def get_notice_detail(
    *,
    db: AsyncSession,
    redis: Redis,
    id: int,
) -> notice_model.NoticeResponse:
    redis_key = REDIS_NOTICE_KEY % id
    notice_data_redis = await notice_logic.get_notice_detail_redis(
        redis=redis, key=redis_key
    )

    if notice_data_redis:
        notice_redis = redis_model.NoticeRedisModel.model_validate(
            obj=notice_data_redis
        )
        return notice_converter.to_NoticeResponse(notice_redis=notice_redis)

    notice_data = await notice_logic.get_notice_detail(db=db, id=id)
    if not notice_data:
        raise exceptions.QueryResultEmpty

    notice = notice_model.NoticeResponse.model_validate(obj=notice_data)
    data = vars(notice_converter.to_NoticeRedisModel(notice_response=notice))
    with redis_db.redis_expire(name=redis_key) as r:
        r.hset(name=redis_key, mapping=data)

    return notice


async def delete_notice(
    *,
    db: AsyncSession,
    redis: Redis,
    id: int,
) -> Awaitable | Any:
    await notice_logic.delete_notice(db=db, id=id)
    redis_res = notice_logic.delete_notice_redis(redis=redis, key=REDIS_NOTICE_KEY % id)
    return redis_res
