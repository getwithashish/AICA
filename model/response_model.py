from typing import Dict
from pydantic import BaseModel


class ResponseModel(BaseModel):
    message: str
    data: Dict
