from datetime import datetime

from ..endpoint.model import notice_model
from ..service.model import service_model


def to_NoticeRedisModel(notice_response: notice_model.NoticeResponse):
    return service_model.NoticeRedisModel(
        id=notice_response.id,
        title=notice_response.title,
        body=notice_response.body,
        created_datetime=notice_response.created_datetime.isoformat(),
    )


def to_NoticeResponse(notice_redis: service_model.NoticeRedisModel):
    return notice_model.NoticeResponse(
        id=notice_redis.id,
        title=notice_redis.title,
        body=notice_redis.body,
        created_datetime=datetime.fromisoformat(notice_redis.created_datetime),
    )
