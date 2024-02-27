import redis
from pydantic import BaseModel, ConfigDict


class RedisModel(BaseModel):
    conn: redis.Redis
    name: str

    model_config = ConfigDict(
        arbitrary_types_allowed=True,
    )
