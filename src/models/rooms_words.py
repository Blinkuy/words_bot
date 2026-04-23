from sqlalchemy import Table, Column, ForeignKey
from src.models.base import Base

rooms_words = Table(
    "rooms_words",
    Base.metadata,
    Column("room_id", ForeignKey("room.id"), primary_key=True),
    Column("word_id", ForeignKey("word.id"), primary_key=True),
)
