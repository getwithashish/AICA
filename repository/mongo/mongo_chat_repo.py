from datetime import datetime
from typing import List
from uuid import UUID

from model.chat_model import ChatModel
from repository.chat_repo import ChatRepo


class MongoChatRepo(ChatRepo):

    @staticmethod
    async def get_chat_by_id(chat_id: UUID = None, user_id: UUID = None):
        # if user_id:
        #     chat = await ChatModel.find_one(
        #         ChatModel.user_id == user_id, ChatModel.chat_id == chat_id
        #     )
        # elif chat_id:
        #     chat = await ChatModel.find_one(ChatModel.chat_id == chat_id)
        # else:
        #     # Raise Error
        #     pass

        chat = await ChatModel.find_one(
            ChatModel.user_id == user_id, ChatModel.chat_id == chat_id
        )

        return chat

    @staticmethod
    async def get_all_chats_of_user(user_id: UUID):
        pass

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
