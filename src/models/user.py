from src.models.base import Base
from sqlalchemy.orm import Mapped, mapped_column, relationship
from sqlalchemy import BigInteger


class User(Base):
    __tablename__ = "user"

    id: Mapped[int] = mapped_column(primary_key=True)
    telegram_id: Mapped[int] = mapped_column(BigInteger, unique=True, index=True)
    is_in_game: Mapped[bool] = mapped_column(default=False)

    room: Mapped["Room"] = relationship(back_populates="users")
