from typing import Any, Awaitable, Iterable

from redis.client import Redis
from sqlalchemy.ext.asyncio import AsyncSession

from src.server.db.entity import NoticeEntity
from src.server.db.query import notice_crud

from ..model import notice_model

REDIS_NOTICE_KEY = "notice:%s"


async def find_notice_by_title(
    *,
    db: AsyncSession,
    data: notice_model.NoticeCreateRequest,
) -> notice_crud.NoticeEntity | None:
    notice = await notice_crud.find_notice_by_title(db=db, title=data.title)
    return notice


async def create_notice(
    *,
    db: AsyncSession,
    data: notice_model.NoticeCreateRequest,
) -> None:
    await notice_crud.create_notice(db=db, title=data.title, body=data.body)


async def get_notice_count(
    *,
    db: AsyncSession,
    keyword: str,
) -> int | None:
    total = await notice_crud.notice_count(db=db, keyword=keyword)
    return total


async def get_notice_list(
    *,
    db: AsyncSession,
    keyword: str,
    page: int,
    size: int,
) -> Iterable[NoticeEntity]:
    notice_list = await notice_crud.notice_list(
        db=db, keyword=keyword, offset=page * size, limit=size
    )
    return notice_list


async def get_notice_detail_redis(
    *,
    redis: Redis,
    key: str,
) -> Awaitable[dict[Any, Any]] | dict[Any, Any]:
    notice_data = redis.hgetall(name=key)
    return notice_data


async def get_notice_detail(
    *,
    db: AsyncSession,
    id: int,
) -> NoticeEntity | None:
    notice_data = await notice_crud.notice_detail(db=db, id=id)
    return notice_data


async def delete_notice(
    *,
    db: AsyncSession,
    id: int,
) -> None:
    await notice_crud.delete_notice(db=db, id=id)


def delete_notice_redis(
    *,
    redis: Redis,
    key: str,
) -> Awaitable | Any:
    res = redis.delete(key)
    return res
