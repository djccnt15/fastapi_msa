from pydantic import BaseModel


class ResponseMsg(BaseModel):
    detail: str


class CreateSuccess(ResponseMsg):
    detail: str = "create success"


class DeleteSuccess(ResponseMsg):
    detail: str = "delete success"
