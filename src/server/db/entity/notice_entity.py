from sqlalchemy.schema import Column
from sqlalchemy.types import DateTime, String

from .base_entity import BigintIdEntity
from .enum import notice_enum


class NoticeEntity(BigintIdEntity):
    __tablename__ = "notice_list"

    title = Column(
        type_=String(notice_enum.NoticeColumnSize.TITLE.value),
        name="title",
        nullable=False,
        unique=True,
    )
    body = Column(
        type_=String(notice_enum.NoticeColumnSize.BODY.value),
        name="body",
        nullable=False,
    )
    created_datetime = Column(
        type_=DateTime,
        name="created_datetime",
        nullable=False,
    )
