from pydantic import BaseModel


class PongModel(BaseModel):
    pong: bool
