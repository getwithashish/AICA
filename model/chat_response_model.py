from datetime import datetime
from typing import Optional
import uuid

from pydantic import field_serializer

from model.chat_message_model import ChatMessageModel, ChatMessageRoleEnum


class ChatResponseModel(ChatMessageModel):
    chatId: uuid.UUID = None
    role: Optional[ChatMessageRoleEnum] = None
    content: str = None

    @field_serializer("chatId")
    def serialize_chat_id(self, id: uuid.UUID, _info):
        return str(id) if id else id

    @field_serializer("timestamp")
    def serialize_timestamp(self, dt: datetime, _info):
        return str(dt) if dt else dt
