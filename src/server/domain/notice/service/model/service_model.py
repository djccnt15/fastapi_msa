from pydantic import ConfigDict

from src.server import common

from ...endpoint.model import notice_model


class NoticeRedisModel(common.IdModel[int], notice_model.NoticeBase):
    created_datetime: str

    model_config = ConfigDict(
        from_attributes=True,
    )
