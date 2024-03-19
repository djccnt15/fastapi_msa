from fastapi import APIRouter, Depends
from sqlalchemy.ext.asyncio import AsyncSession
from starlette import status

from src.server import common, database

from ..business import notice_process
from ..model import notice_model

router = APIRouter(prefix="/notice")


@router.post(path="/", status_code=status.HTTP_201_CREATED)
async def create_notice(
    data: notice_model.NoticeCreateRequest,
    db: AsyncSession = Depends(database.get_db),
) -> common.CreateSuccess:
    await notice_process.create_notice(db=db, data=data)
    return common.CreateSuccess()


@router.get(path="/list")
async def notice_list(
    keyword: str = "",
    page: int = 0,
    size: int = 10,
    db: AsyncSession = Depends(database.get_db),
) -> notice_model.NoticeList:
    notice_list = await notice_process.get_notice_list(
        db=db, keyword=keyword, page=page, size=size
    )
    return notice_list


@router.get(path="/{id}")
async def notice_detail(
    id: int,
    db: AsyncSession = Depends(database.get_db),
) -> notice_model.NoticeResponse:
    notice_detail = await notice_process.get_notice_detail(db=db, id=id)
    return notice_detail


@router.delete(path="/{id}")
async def notice_delete(
    id: int,
    db: AsyncSession = Depends(database.get_db),
) -> common.DeleteSuccess:
    await notice_process.delete_notice(db=db, id=id)
    return common.DeleteSuccess()
