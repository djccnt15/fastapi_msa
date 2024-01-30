import redis

from src.server import configs

config = configs.config.redis

rd = redis.Redis(
    host=config.host,
    port=config.port,
    decode_responses=config.decode_responses,
)
