from advanced_alchemy.service import SQLAlchemyAsyncRepositoryService
from src.models.user import User
from src.repositories.user import UserRepository


class UserService(SQLAlchemyAsyncRepositoryService[User]):
    repository_type = UserRepository

    async def register_user(self, telegram_id) -> tuple[User, bool]:

        user, is_new = await self.repository.get_or_create(telegram_id)

        return user, is_new
