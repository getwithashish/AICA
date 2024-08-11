from enum import Enum
from typing import Optional
import uuid
from pydantic import BaseModel


class ChatResponseRoleEnum(str, Enum):
    tool = "tool"
    tool_resposne = "tool_response"
    human = "human"
    assistant = "assistant"


class ChatResponseModel(BaseModel):
    chatId: Optional[uuid.UUID]
    role: ChatResponseRoleEnum = ChatResponseRoleEnum.assistant
    content: str
    timestamp: str
    confidence: float
