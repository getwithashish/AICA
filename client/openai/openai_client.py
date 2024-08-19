from typing import List
from openai import AsyncOpenAI
from openai.types.chat.chat_completion import Choice

from client.ai_client import AIClient
from client.openai.config import MODEL_NAME, OPENAI_API_BASE, USER_ROLE_NAME


class OpenAIClient(AIClient):

    def __init__(self, model_name=MODEL_NAME):
        self.model_name = model_name
        self.client = AsyncOpenAI(base_url=OPENAI_API_BASE)

    async def infer_from_text(self, messages: List) -> Choice:
        chat_completion = await self.client.chat.completions.create(
            messages=messages,
            model=f"{self.model_name}",
        )
        return chat_completion.choices[0]

    @staticmethod
    def chat_message_formatter(chat_messages: List) -> List:
        # TODO Write logic for formatting the messages compatible for OpenAI
        # TODO Remove messages with role "tool" and "tool_response"
        # messages = (
        #     [
        #         {
        #             "role": f"{self.user_role_name}",
        #             "content": f"{prompt}",
        #         }
        #     ],
        # )

        user_role_name = USER_ROLE_NAME
        messages = [
            {
                "role": f"{user_role_name}",
                "content": "What is SFM?",
            }
        ]
        return messages

    @staticmethod
    def ai_response_formatter(response):
        return response.message.content

    @staticmethod
    def ai_response_confidence_calculator(response):
        pass
