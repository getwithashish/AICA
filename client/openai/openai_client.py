from typing import List
from openai import AsyncOpenAI
from openai.types.chat.chat_completion import Choice
import numpy as np
from pydantic import BaseModel

from client.ai_client import AIClient
from client.openai.config import (
    ASSISTANT_ROLE_NAME,
    MODEL_NAME,
    OPENAI_API_BASE,
    OPENAI_KEY,
    USER_ROLE_NAME,
)
from model.chat_message_model import ChatMessageRoleEnum
from util.chat_message_formatter import ChatMessageFormatter


class OpenAIClient(AIClient):

    def __init__(self, model_name=MODEL_NAME):
        self.model_name = model_name
        self.client = AsyncOpenAI(base_url=OPENAI_API_BASE, api_key=OPENAI_KEY)

    async def infer_from_text(self, messages: List) -> Choice:
        # class Dummy_Dict_Data(BaseModel):
        #     content: str = "Hello, How are you?"

        # class Dummy_Dict(BaseModel):
        #     message: Dummy_Dict_Data = Dummy_Dict_Data()

        # ai_dummy_value = Dummy_Dict()
        # return ai_dummy_value.model_dump()
        chat_completion = await self.client.chat.completions.create(
            messages=messages,
            model=f"{self.model_name}",
            temperature=0.1,
            logprobs=True,
        )
        return chat_completion.choices[0]

    @staticmethod
    def format_chat_message(messages: List) -> List:
        messages = ChatMessageFormatter.remove_tool_messages(chat_messages=messages)

        formatted_messages = []
        for message in messages:
            message_dict = message.model_dump(exclude={"timestamp", "confidence"})
            if message_dict["role"] == ChatMessageRoleEnum.human:
                message_dict["role"] = USER_ROLE_NAME
            elif message_dict["role"] == ChatMessageRoleEnum.assistant:
                message_dict["role"] = ASSISTANT_ROLE_NAME
            formatted_messages.append(message_dict)

        return formatted_messages

    @staticmethod
    def format_ai_response(response: Choice) -> str:
        # return response["message"]["content"]
        return response.message.content

    @staticmethod
    def calculate_ai_response_confidence(response: Choice) -> float:
        # return 70.0
        logprobs: List[float] = []
        token_logprobs = response.logprobs.content
        for token_logprob in token_logprobs:
            logprobs.append(token_logprob.logprob)

        total_logprob = sum(logprobs)
        probability = np.exp(total_logprob)
        max_length = 100
        confidence_score = probability ** (1 / max_length)
        confidence_score_percentage = confidence_score * 100

        return confidence_score_percentage
