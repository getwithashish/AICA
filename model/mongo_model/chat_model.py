from datetime import datetime
from typing import List
from uuid import UUID, uuid4
from beanie import Document
from pydantic import Field

from model.chat_message_model import ChatMessageModel


class ChatModel(Document):
    user_id: UUID
    chat_id: UUID = Field(default_factory=uuid4)
    chat_title: str
    updated_at: datetime
    messages: List[ChatMessageModel]

    class Settings:
        name = "chat_collection"
        indexes = [
            {"fields": ["user_id"], "unique": True},
            {"fields": ["updated_at"]},
            {"fields": ["user_id", "created_at"]},  # Compound index
        ]
        keep_nulls = False
