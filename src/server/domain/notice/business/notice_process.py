from sqlalchemy.ext.asyncio import AsyncSession

from src.server.common import exception

from ..endpoint.model import notice_model
from ..service import notice_logic


async def create_notice(
    *,
    db: AsyncSession,
    data: notice_model.NoticeCreateRequest,
):
    notice = await notice_logic.find_notice_by_title(db=db, data=data)
    if notice:
        raise exception.NotUniqueException(obj="title", detail=data.title)
    await notice_logic.create_notice(db=db, data=data)


async def get_notice_list(
    *,
    db: AsyncSession,
    keyword: str,
    page: int,
    size: int,
):
    notice_list = await notice_logic.get_notice_list(
        db=db, keyword=keyword, page=page, size=size
    )
    return notice_list


async def get_notice_detail(
    *,
    db: AsyncSession,
    id: int,
):
    notice_detail = await notice_logic.get_notice_detail(db=db, id=id)
    return notice_detail


async def delete_notice(
    *,
    db: AsyncSession,
    id: int,
):
    await notice_logic.delete_notice(db=db, id=id)
