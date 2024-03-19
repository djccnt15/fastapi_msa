from pydantic import ConfigDict

from src.server import common

from . import notice_model


class NoticeRedisModel(common.IdModel[int], notice_model.NoticeBase):
    model_config = ConfigDict(
        from_attributes=True,
    )

    created_datetime: str
