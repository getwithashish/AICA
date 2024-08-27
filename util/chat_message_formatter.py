from typing import List

from model.chat_message_model import ChatMessageRoleEnum


class ChatMessageFormatter:

    @staticmethod
    def remove_tool_messages(chat_messages: List) -> List:
        messages = []
        for chat_message in chat_messages:
            if chat_message.role not in (
                ChatMessageRoleEnum.tool,
                ChatMessageRoleEnum.tool_response,
            ):
                messages.append(chat_message)
        return messages
