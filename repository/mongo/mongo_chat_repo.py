from datetime import datetime
from typing import List
from uuid import UUID

from model.chat_model import ChatModel
from repository.chat_repo import ChatRepo


class MongoChatRepo(ChatRepo):

    @staticmethod
    async def get_chat_by_id(chat_id: UUID = None, user_id: UUID = None):
        chat = await ChatModel.find_one(
            ChatModel.user_id == user_id, ChatModel.chat_id == chat_id
        )

        return chat

    @staticmethod
    async def get_all_chats_of_user(user_id: UUID):
        chats = await ChatModel.find(ChatModel.user_id == user_id).to_list()
        return chats

    @staticmethod
    async def save_new_chat(chat: ChatModel) -> ChatModel:
        chat = await chat.insert()
        return chat

    @staticmethod
    async def update_chat(chat: ChatModel, updated_at: datetime, messages: List):
        await chat.update(
            {
                "$set": {
                    ChatModel.updated_at: updated_at,
                },
                "$push": {ChatModel.messages: {"$each": messages}},
            }
        )
