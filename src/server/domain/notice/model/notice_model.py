from datetime import datetime
from typing import Iterable

from pydantic import BaseModel, ConfigDict, Field

from src.server.core.model import common_model
from src.server.db.entity.enum import notice_enum


class NoticeBase(BaseModel):
    title: str
    body: str


class NoticeCreateRequest(NoticeBase):
    title: str = Field(max_length=notice_enum.NoticeColumnSize.TITLE)
    body: str = Field(max_length=notice_enum.NoticeColumnSize.BODY)


class NoticeResponse(common_model.IdModel[int], NoticeBase):
    model_config = ConfigDict(
        from_attributes=True,
    )

    created_datetime: datetime


class NoticeListResponse(BaseModel):
    total: int
    notice_list: Iterable[NoticeResponse]
