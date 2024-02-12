import redis
from pydantic import BaseModel


class RedisModel(BaseModel):
    conn: redis.Redis
    name: str
