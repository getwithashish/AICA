from abc import ABC, abstractmethod
from typing import List

from model.chat_request_model import ChatRequestDataModel


class AIClient(ABC):
    """
    This module provides the skeleton for AI Clients
    """

    @abstractmethod
    async def infer_from_text(self, messages: List):
        """
        Infers the response from the list of messages, by using the AI Model

        Args:
            messages (List): The list of messages from which the inference must be performed
        """
        pass

    @staticmethod
    @abstractmethod
    def chat_message_formatter(messages: List[ChatRequestDataModel]):
        """
        Transforms the received request messages to a format understood by the AI Client

        Args:
            messages (List[ChatRequestDataModel]): The list of messages to be formatted
        """
        pass

    @staticmethod
    @abstractmethod
    def ai_response_formatter(response: object):
        """
        Transforms the inference from AI client to a format that can be used by the application

        Args:
            response (object): The inference along with the corresponding metadata
        """
        pass

    @staticmethod
    @abstractmethod
    def ai_response_confidence_calculator(response: object):
        """
        Calculates the confidence score of the inference from AI Client

        Args:
            response (object): The inference along with the corresponding metadata
        """
        pass
