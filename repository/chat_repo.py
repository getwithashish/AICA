from uuid import UUID

from model.mongo_model.chat_model import ChatModel


class ChatRepo:

    @staticmethod
    async def get_chat_by_id(chat_id: UUID, user_id: UUID = None):
        if user_id and chat_id:
            chat = await ChatModel.find_one(
                ChatModel.user_id == user_id, ChatModel.chat_id == chat_id
            )
        elif chat_id:
            chat = await ChatModel.find_one(ChatModel.chat_id == chat_id)
        else:
            # Raise Error
            pass

        return chat

    @staticmethod
    async def get_all_chats_of_user(user_id: UUID):
        pass
