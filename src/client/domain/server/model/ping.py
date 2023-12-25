from pydantic import BaseModel


class PongModel(BaseModel):
    status: int
    body: str
