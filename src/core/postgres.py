from sqlalchemy import create_engine
from sqlalchemy.orm import registry, sessionmaker

from core.settings import settings

database_url: str = f"{settings.DATABASE_DRIVERNAME}://\
    {settings.POSTGRES_USER}:{settings.POSTGRES_PASSWORD}@\
    {settings.POSTGRES_HOST}:{str(settings.POSTGRES_PORT)}/\
    {settings.POSTGRES_DB}"

database_url = database_url.replace(" ", "").replace("\n", "")


engine = create_engine(url=database_url, echo=settings.DEBUG)

LocalSession = sessionmaker(bind=engine)

mapper_registry = registry()
