from enum import Enum
from typing import Optional
from pydantic import BaseModel
from datetime import datetime


class ChatMessageRoleEnum(str, Enum):
    tool = "tool"
    tool_response = "tool_response"
    human = "human"
    assistant = "assistant"


class ChatMessageModel(BaseModel):
    role: ChatMessageRoleEnum = ChatMessageRoleEnum.assistant
    content: str
    timestamp: datetime = datetime.now()
    confidence: Optional[float] = None
