from datetime import datetime

from pydantic import BaseModel, ConfigDict, Field

from src.server import common, db


class NoticeBase(BaseModel):
    title: str
    body: str


class NoticeCreateRequest(NoticeBase):
    title: str = Field(max_length=db.NoticeColumnSize.TITLE)
    body: str = Field(max_length=db.NoticeColumnSize.BODY)


class NoticeResponse(common.Id[int], NoticeBase):
    created_datetime: datetime

    model_config = ConfigDict(
        from_attributes=True,
    )


class NoticeList(BaseModel):
    total: int
    notice_list: list[NoticeResponse]
