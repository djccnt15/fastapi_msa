from pydantic import ConfigDict

from src.server.common.model import common_model

from . import notice_model


class NoticeRedisModel(common_model.IdModel[int], notice_model.NoticeBase):
    model_config = ConfigDict(
        from_attributes=True,
    )

    created_datetime: str
