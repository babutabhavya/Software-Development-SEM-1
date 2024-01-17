from pydantic import BaseModel


class ResponseModel(BaseModel):
    message: str
    status_code: int
