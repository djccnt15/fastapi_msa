from contextlib import contextmanager
from datetime import timedelta

import redis

from src.server import configs

from .model import redis_model

config = configs.config.redis

redis_db = redis.Redis(**config)


@contextmanager
def redis_conn(
    *,
    name: str,
    expire_time: int | timedelta = 30,
):
    try:
        yield redis_model.RedisModel(conn=redis_db, name=name)
    finally:
        redis_db.expire(name=name, time=expire_time)
