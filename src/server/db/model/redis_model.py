import redis
from pydantic import BaseModel, ConfigDict


class RedisModel(BaseModel):
    model_config = ConfigDict(
        arbitrary_types_allowed=True,
    )

    conn: redis.Redis
    name: str
