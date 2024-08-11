from enum import Enum
from typing import List, Optional
import uuid
from pydantic import BaseModel


class ChatRequestRoleEnum(str, Enum):
    tool = "tool"
    tool_resposne = "tool_response"
    human = "human"


class ChatRequestDataModel(BaseModel):
    role: ChatRequestRoleEnum
    content: str

    # @field_validator("role")
    # def role_must_not_be_empty(cls, role_value):
    #     if not role_value.strip():
    #         raise ValueError("Role must not be empty")
    #     return role_value


class ChatRequestModel(BaseModel):
    chatId: Optional[uuid.UUID] = None
    data: List[ChatRequestDataModel]
