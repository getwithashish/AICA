from uuid import UUID

from model.chat_model import ChatModel
from repository.user_repo import UserRepo


class MongoUserRepo(UserRepo):

    @staticmethod
    async def check_user_id_exists(user_id: UUID) -> bool:
        user_exists = await ChatModel.find_one(ChatModel.user_id == user_id).exists()
        return user_exists
