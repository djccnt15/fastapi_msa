from sqlalchemy.ext.asyncio import AsyncSession

from src.server.common.exception import exceptions
from src.server.db import redis_db
from src.server.db.query import notice_crud

from ..converter import notice_converter
from ..model import notice_model, redis_model

REDIS_NOTICE_KEY = "notice:%s"


async def find_notice_by_title(
    *,
    db: AsyncSession,
    data: notice_model.NoticeCreateRequest,
):
    notice = await notice_crud.find_notice_by_title(db=db, title=data.title)
    return notice


async def create_notice(
    *,
    db: AsyncSession,
    data: notice_model.NoticeCreateRequest,
):
    await notice_crud.create_notice(db=db, title=data.title, body=data.body)


async def get_notice_list(
    *,
    db: AsyncSession,
    keyword: str,
    page: int,
    size: int,
):
    total = await notice_crud.notice_count(db=db, keyword=keyword)
    if not total:
        raise exceptions.QueryResultEmpty
    notice_list = await notice_crud.notice_list(
        db=db, keyword=keyword, offset=page * size, limit=size
    )
    response_list = (
        notice_model.NoticeResponse.model_validate(obj=x) for x in notice_list
    )
    return notice_model.NoticeList(
        total=total,
        notice_list=response_list,
    )


async def get_notice_detail(
    *,
    db: AsyncSession,
    id: int,
):
    redis_key = REDIS_NOTICE_KEY % id
    notice_data = redis_db.redis_db.hgetall(name=redis_key)

    if notice_data:
        notice_redis = redis_model.NoticeRedisModel.model_validate(obj=notice_data)
        return notice_converter.to_NoticeResponse(notice_redis=notice_redis)

    notice_data = await notice_crud.notice_detail(db=db, id=id)
    if notice_data:
        notice = notice_model.NoticeResponse.model_validate(obj=notice_data)
        data = vars(notice_converter.to_NoticeRedisModel(notice_response=notice))
        with redis_db.redis_conn(name=redis_key) as r:
            r.conn.hset(name=r.name, mapping=data)
        return notice
    raise exceptions.QueryResultEmpty


async def delete_notice(
    *,
    db: AsyncSession,
    id: int,
):
    await notice_crud.delete_notice(db=db, id=id)
    redis_db.redis_db.delete(REDIS_NOTICE_KEY % id)
