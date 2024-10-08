from typing import List
import uuid

from pydantic import BaseModel, field_serializer

from model.chat_model import ChatModel


class ChatListResponseModel(BaseModel):
    userId: uuid.UUID = None
    chats: List[ChatModel] = None

    @field_serializer("userId")
    def serialize_user_id(self, id: uuid.UUID, _info):
        return str(id) if id else id
