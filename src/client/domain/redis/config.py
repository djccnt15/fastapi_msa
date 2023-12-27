import redis

from src.client import configs

config = configs.config.redis

rd = redis.Redis(
    host=config.host,
    port=config.port,
    decode_responses=config.decode_responses,
)
