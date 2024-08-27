from typing import List
from uuid import UUID

from fastapi.exceptions import RequestValidationError

from model.chat_model import ChatModel
from repository.chat_repo import ChatRepo
from repository.user_repo import UserRepo
from util.missing_dict_keys_finder import MissingDictKeysFinder


class ChatHistoryService:

    def __init__(self, chat_repo: ChatRepo, user_repo: UserRepo):
        self.chat_repo = chat_repo
        self.user_repo = user_repo

    async def save_chat_to_history(self, chat: ChatModel, chat_exists: bool, **kwargs):
        if chat_exists:
            required_keys = {"updated_at", "messages"}
            missing_keys = MissingDictKeysFinder.find_missing_keys(
                required_keys=required_keys, **kwargs
            )
            if missing_keys:
                raise RequestValidationError(f"Does not contain {required_keys}")
            else:
                await self.chat_repo.update_chat(
                    chat=chat,
                    updated_at=kwargs["updated_at"],
                    messages=kwargs["messages"],
                )
        else:
            required_keys = {"chat_title", "updated_at", "messages"}
            missing_keys = MissingDictKeysFinder.find_missing_keys(
                required_keys=required_keys, **kwargs
            )
            if missing_keys:
                raise RequestValidationError(f"Does not contain {required_keys}")
            else:
                chat.chat_title = kwargs["chat_title"]
                chat.updated_at = kwargs["updated_at"]
                chat.messages = kwargs["messages"]
                chat = await self.chat_repo.save_new_chat(chat)

    async def get_chat_history(self, user_id: UUID, chat_id: UUID) -> ChatModel:
        chat = await self.chat_repo.get_chat_by_id(chat_id=chat_id, user_id=user_id)
        return chat

    async def get_chat_messages(self, user_id: UUID, chat_id: UUID) -> List:
        chat = await self.get_chat_history(user_id=user_id, chat_id=chat_id)
        return chat.messages if chat else []
