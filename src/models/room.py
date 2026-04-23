from sqlalchemy.orm import Mapped, mapped_column, relationship
from src.models.base import Base
from src.models.rooms_words import rooms_words


class Room(Base):
    __tablename__ = "room"

    id: Mapped[int] = mapped_column(primary_key=True)
    is_active: Mapped[bool]

    users: Mapped[list["User"]] = relationship(back_populates="room")
    words: Mapped[list["Word"]] = relationship(secondary=rooms_words)
