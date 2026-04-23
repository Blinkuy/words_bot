from src.models.base import Base
from sqlalchemy.orm import Mapped, mapped_column, relationship


class Word(Base):
    id: Mapped[int] = mapped_column(primary_key=True)
    word: Mapped[str] = mapped_column(unique=True)
