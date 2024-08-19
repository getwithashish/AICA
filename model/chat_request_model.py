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


class ChatRequestModel(BaseModel):
    chatId: Optional[uuid.UUID] = None
    data: List[ChatRequestDataModel]
