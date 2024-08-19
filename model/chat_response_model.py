import uuid

from model.chat_message_model import ChatMessageModel


class ChatResponseModel(ChatMessageModel):
    chatId: uuid.UUID
