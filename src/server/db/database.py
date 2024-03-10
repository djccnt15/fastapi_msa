from sqlalchemy.engine import URL
from sqlalchemy.ext.asyncio import AsyncSession, create_async_engine

from src.server import configs

db_config = configs.config.db

engine = create_async_engine(
    url=URL.create(**db_config.url),
    **db_config.engine,
)


async def get_db():
    db = AsyncSession(bind=engine)
    try:
        yield db
    finally:
        await db.close()
