from abc import ABC, abstractmethod
from typing import List

from model.chat_request_model import ChatRequestDataModel


class AIClient(ABC):

    @abstractmethod
    async def infer_from_text(self, messages: List):
        pass

    @staticmethod
    @abstractmethod
    def chat_message_formatter(messages: List[ChatRequestDataModel]):
        pass

    @staticmethod
    @abstractmethod
    def ai_response_formatter(response: object):
        pass

    @staticmethod
    @abstractmethod
    def ai_response_confidence_calculator(response: object):
        pass
