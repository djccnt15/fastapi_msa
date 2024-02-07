from datetime import datetime

from sqlalchemy.ext.asyncio import AsyncSession
from sqlalchemy.sql import delete, func, insert, select

from ..entity import NoticeEntity


async def create_notice(
    db: AsyncSession,
    title: str,
    body: str,
):
    q = insert(NoticeEntity).values(
        title=title,
        body=body,
        created_datetime=datetime.now(),
    )
    await db.execute(q)
    await db.commit()


async def find_notice_by_title(
    db: AsyncSession,
    title: str,
):
    q = select(NoticeEntity).where(NoticeEntity.title == title)
    result = await db.execute(q)
    return result.scalar()


async def notice_count(
    db: AsyncSession,
    keyword: str,
):
    q = select(NoticeEntity)
    if keyword:
        keyword = f"%{keyword}%"
        q = q.where(
            NoticeEntity.title.ilike(keyword) | NoticeEntity.body.ilike(keyword)
        )
    total = await db.execute(select(func.count()).select_from(q))
    return total.scalar()


async def notice_list(
    db: AsyncSession,
    keyword: str,
    offset: int,
    limit: int,
):
    q = select(NoticeEntity)
    if keyword:
        keyword = f"%{keyword}%"
        q = q.where(
            NoticeEntity.title.ilike(keyword) | NoticeEntity.body.ilike(keyword)
        )
    q = q.order_by(NoticeEntity.created_datetime.desc()).offset(offset).limit(limit)
    res = await db.execute(q)
    return res.scalars()


async def notice_detail(
    db: AsyncSession,
    id: int,
):
    q = select(NoticeEntity).where(NoticeEntity.id == id)
    res = await db.execute(q)
    return res.scalar()


async def delete_notice(
    db: AsyncSession,
    id: int,
):
    q = delete(NoticeEntity).where(NoticeEntity.id == id)
    await db.execute(q)
    await db.commit()
