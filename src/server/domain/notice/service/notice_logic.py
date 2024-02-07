from sqlalchemy.ext.asyncio import AsyncSession

from src.server.common import exception
from src.server.db import notice_crud

from ..endpoint.model import notice_model


async def find_notice_by_title(
    db: AsyncSession,
    data: notice_model.NoticeCreateRequest,
):
    notice = await notice_crud.find_notice_by_title(db=db, title=data.title)
    return notice


async def create_notice(
    db: AsyncSession,
    data: notice_model.NoticeCreateRequest,
):
    await notice_crud.create_notice(db=db, title=data.title, body=data.body)


async def get_notice_list(
    db: AsyncSession,
    keyword: str,
    page: int,
    size: int,
):
    total: int = await notice_crud.notice_count(db=db, keyword=keyword)
    if not total:
        raise exception.QueryResultEmpty
    notice_list = await notice_crud.notice_list(
        db=db, keyword=keyword, offset=page * size, limit=size
    )
    return notice_model.NoticeList(
        total=total,
        notice_list=notice_list,  # type: ignore
    )


async def get_notice_detail(
    db: AsyncSession,
    id: int,
):
    notice_data = await notice_crud.notice_detail(db=db, id=id)
    if notice_data:
        notice = notice_model.NoticeResponse.model_validate(notice_data)
        return notice
    raise exception.QueryResultEmpty


async def delete_notice(
    db: AsyncSession,
    id: int,
):
    await notice_crud.delete_notice(db=db, id=id)
