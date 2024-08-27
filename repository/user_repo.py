from abc import ABC, abstractmethod
from uuid import UUID


class UserRepo(ABC):

    @staticmethod
    @abstractmethod
    async def check_user_id_exists(user_id: UUID) -> bool:
        """
        Check whether the User ID exists or not

        Args:
            user_id (UUID): ID of the User

        Returns:
            bool: True if user exists, else False
        """
        pass
