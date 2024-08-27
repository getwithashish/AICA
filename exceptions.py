from uuid import UUID


class InvalidDataException(Exception):
    def __init__(self, message: str):
        self.message = message


class UnauthorizedUserException(Exception):
    def __init__(self, message: str):
        self.message = message


class ChatSessionNotFoundException(Exception):
    def __init__(self, chat_id: UUID):
        self.chat_id = chat_id
