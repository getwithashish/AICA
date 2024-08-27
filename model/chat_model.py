from datetime import datetime
from typing import List, Optional
from uuid import UUID, uuid4
from beanie import Document
from pydantic import Field

from model.chat_message_model import ChatMessageModel


class ChatModel(Document):
    user_id: UUID
    chat_id: UUID = Field(default_factory=uuid4)
    chat_title: Optional[str]
    updated_at: Optional[datetime]
    messages: Optional[List[ChatMessageModel]]

    class Settings:
        name = "chat_collection"
        keep_nulls = False
