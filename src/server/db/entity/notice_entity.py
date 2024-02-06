from sqlalchemy.schema import Column
from sqlalchemy.types import DateTime, String

from .base_entity import BaseEntity
from .enum import NoticeColumnSize


class NoticeEntity(BaseEntity):
    __tablename__ = "notice_list"

    title = Column(
        type_=String(NoticeColumnSize.TITLE.value),
        name="title",
        nullable=False,
        unique=True,
    )
    body = Column(
        type_=String(NoticeColumnSize.BODY.value),
        name="body",
        nullable=False,
    )
    created_datetime = Column(
        type_=DateTime,
        name="created_datetime",
        nullable=False,
    )
