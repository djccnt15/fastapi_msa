from contextlib import contextmanager
from datetime import timedelta

import redis

from src.server import configs

from .model import redis_model

config = configs.config.redis

redis_db = redis.Redis(
    host=config.host,
    port=config.port,
    decode_responses=config.decode_responses,
)


@contextmanager
def redis_conn(name: str, expire_time: int | timedelta):
    try:
        yield redis_model.RedisModel(conn=redis_db, name=name)
    finally:
        if expire_time:
            redis_db.expire(name=name, time=expire_time)
