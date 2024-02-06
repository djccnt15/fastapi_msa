from sqlalchemy.engine import URL
from sqlalchemy.ext.asyncio import AsyncSession, create_async_engine

from src.server import configs

db_config = configs.config.db

SQLALCHEMY_DATABASE_URL = URL.create(
    drivername=db_config.drivername,
    username=db_config.username if db_config.username else None,
    password=db_config.password if db_config.password else None,
    host=db_config.host if db_config.host else None,
    port=int(db_config.port) if db_config.port else None,
    database=db_config.database,
)

engine = create_async_engine(
    url=SQLALCHEMY_DATABASE_URL,
    pool_pre_ping=True,
    pool_recycle=3600,
    echo=db_config.echo,
)


async def get_db():
    db = AsyncSession(bind=engine)
    try:
        yield db
    finally:
        await db.close()