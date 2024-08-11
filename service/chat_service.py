from datetime import datetime
from typing import List

from client.ai_client import AIClient
from model.chat_response_model import ChatResponseModel


class ChatService:

    @staticmethod
    async def infer_from_text(messages: List, ai_client: AIClient):
        chat_completion = await ai_client.infer_from_text(messages)
        ai_response = ai_client.ai_response_formatter(chat_completion)
        confidence_score = ai_client.ai_response_confidence_calculator(chat_completion)
        current_timestamp = datetime.now()
        chat_response_model = ChatResponseModel(
            content=ai_response,
            timestamp=current_timestamp,
            confidence=confidence_score,
        )
        return chat_response_model
