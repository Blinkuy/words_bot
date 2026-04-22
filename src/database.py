from sqlalchemy.ext.asyncio import create_async_engine, async_sessionmaker
from src.config import settings
from contextlib import asynccontextmanager

engine = create_async_engine(url=settings.DATABASE_URL, echo=True)

SessionLocal = async_sessionmaker(engine, expire_on_commit=False)


@asynccontextmanager
async def get_session():
    async with SessionLocal() as session:
        yield session
