import asyncio
from datetime import datetime
from typing import List, Optional
from uuid import UUID

from client.ai_client import AIClient
from client.openai.config import TITLE_PROMPT
from exceptions import ChatSessionNotFoundException, UnauthorizedUserException
from messages import USER_DOES_NOT_EXIST
from model.chat_list_response_model import ChatListResponseModel
from model.chat_message_model import ChatMessageModel
from model.chat_request_model import ChatRequestDataModel, ChatRequestRoleEnum
from model.chat_response_model import ChatResponseModel
from model.chat_model import ChatModel
from repository.chat_repo import ChatRepo
from repository.user_repo import UserRepo
from service.chat_history_service import ChatHistoryService


class ChatService:

    @staticmethod
    async def initiate_chat(
        user_id: UUID,
        chat_id: Optional[UUID],
        chat_request_messages: List[ChatRequestDataModel],
        ai_client: AIClient,
        chat_repo: ChatRepo,
        user_repo: UserRepo,
    ):

        new_messages: List[ChatMessageModel] = []
        chat_exists = True
        chat_title = ""
        chat_response = ChatResponseModel()
        chat_history_service = ChatHistoryService(
            chat_repo=chat_repo, user_repo=user_repo
        )

        # Convert Chat Request Message to Chat Message
        for chat_request_message in chat_request_messages:
            current_timestamp = datetime.now()
            chat_message_model = ChatMessageModel(
                role=chat_request_message.role,
                content=chat_request_message.content,
                timestamp=current_timestamp,
            )
            new_messages.append(chat_message_model)

        chat = await chat_history_service.get_chat_history(
            user_id=user_id, chat_id=chat_id
        )
        if not chat:
            # Raise error if the provided chat_id is not found
            if chat_id:
                raise ChatSessionNotFoundException(chat_id=chat_id)
            chat_exists = False
            chat = ChatModel(
                user_id=user_id, chat_title=None, updated_at=None, messages=None
            )
            # Generates Chat Title in Background
            chat_title_task = asyncio.create_task(
                ChatService.initiate_inference(
                    messages=new_messages, ai_client=ai_client, generate_chat_title=True
                )
            )

        chat_history_messages = chat.messages if chat.messages else []

        # Infer using AI Client if the new message author is a human
        if any(
            new_message.role == ChatRequestRoleEnum.human.value
            for new_message in new_messages
        ):
            ai_chat_response = await ChatService.initiate_inference(
                messages=chat_history_messages + new_messages, ai_client=ai_client
            )
            new_messages.append(ai_chat_response)

            # Populate the Chat Response Model for giving back to user
            chat_response.role = ai_chat_response.role
            chat_response.content = ai_chat_response.content
            chat_response.confidence = ai_chat_response.confidence

        latest_message_timestamp = new_messages[-1].timestamp

        if not chat_exists:
            chat_title_response = await chat_title_task
            chat_title = chat_title_response.content

        # Populate the Chat Response Model for giving back to user
        chat_response.timestamp = latest_message_timestamp
        chat_response.chatId = chat.chat_id

        await chat_history_service.save_chat_to_history(
            chat=chat,
            chat_exists=chat_exists,
            chat_title=chat_title,
            updated_at=latest_message_timestamp,
            messages=new_messages,
        )

        return chat_response

    @staticmethod
    async def initiate_inference(
        messages: List, ai_client: AIClient, generate_chat_title: bool = False
    ) -> ChatMessageModel:
        chat_messages = list(messages)
        if generate_chat_title:
            title_generator_message = ChatRequestDataModel(
                role=ChatRequestRoleEnum.human,
                content=TITLE_PROMPT,
            )
            chat_messages.append(title_generator_message)

        formatted_prompt_messages = ai_client.format_chat_message(messages=chat_messages)
        ai_chat_response = await ChatService.infer_from_text(
            messages=formatted_prompt_messages, ai_client=ai_client
        )
        return ai_chat_response

    @staticmethod
    async def infer_from_text(messages: List, ai_client: AIClient) -> ChatMessageModel:
        chat_completion = await ai_client.infer_from_text(messages)
        ai_response = ai_client.format_ai_response(chat_completion)
        confidence_score = ai_client.calculate_ai_response_confidence(chat_completion)
        current_timestamp = datetime.now()
        chat_response_model = ChatMessageModel(
            content=ai_response,
            timestamp=current_timestamp,
            confidence=confidence_score,
        )
        return chat_response_model

    @staticmethod
    async def find_chats_by_user(
        user_id: str, chat_repo: ChatRepo, user_repo: UserRepo
    ) -> ChatListResponseModel:
        if not await user_repo.check_user_id_exists(user_id=user_id):
            raise UnauthorizedUserException(USER_DOES_NOT_EXIST)

        chats = await chat_repo.get_all_chats_of_user(user_id=user_id)
        chat_list = ChatListResponseModel(userId=user_id, chats=chats)
        return chat_list
