from advanced_alchemy.repository import SQLAlchemyAsyncRepository
from src.models.user import User


class UserRepository(SQLAlchemyAsyncRepository[User]):
    model_type = User

    async def get_or_create(self, telegram_id: int) -> tuple[User | None, bool]:
        user = await self.get_one_or_none(telegram_id=telegram_id)

        if user:
            return user, False

        user = await self.add(User(telegram_id=telegram_id))

        await self.session.commit()

        return user, True
