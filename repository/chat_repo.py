from abc import ABC, abstractmethod
from datetime import datetime
from typing import List
from uuid import UUID

from model.chat_model import ChatModel


class ChatRepo(ABC):
    """
    Abstract Base Repository Class for Chat
    """

    @staticmethod
    @abstractmethod
    async def get_chat_by_id(chat_id: UUID, user_id: UUID = None) -> ChatModel:
        """
        Get the Chat by User ID and Chat ID. If the User ID is None, then the chat is fetched by using only the Chat ID

        Args:
            chat_id (UUID): ID of the Chat
            user_id (UUID, optional): ID of the User. Defaults to None.
        """
        pass

    @staticmethod
    @abstractmethod
    async def get_all_chats_of_user(user_id: UUID) -> List[ChatModel]:
        """
        Get all the chats of the user

        Args:
            user_id (UUID): ID of the User
        """
        pass

    @staticmethod
    @abstractmethod
    async def save_new_chat(chat: ChatModel):
        """
        Save the new chat

        Args:
            chat (ChatModel): New Chat to be saved
        """
        pass

    @staticmethod
    @abstractmethod
    async def update_chat(chat: ChatModel, updated_at: datetime, messages: List):
        """
        Update and existing chat

        Args:
            chat (ChatModel): Existing chat that is to be updated
            updated_at (datetime): The timestamp of the latest chat message
            messages (List): The list of new chat messages
        """
        pass
