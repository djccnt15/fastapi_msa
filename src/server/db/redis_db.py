from contextlib import contextmanager
from datetime import timedelta

from redis.client import Redis
from redis.connection import ConnectionPool

from src.server import configs

config = configs.config.redis

redis_pool = ConnectionPool(**config)


def get_redis():
    r = Redis.from_pool(connection_pool=redis_pool)
    try:
        yield r
    finally:
        r.close()


@contextmanager
def redis_expire(
    *,
    name: str,
    time: int | timedelta = 30,
):
    r = Redis.from_pool(connection_pool=redis_pool)
    try:
        yield r
    finally:
        r.expire(name=name, time=time)
        r.close()
