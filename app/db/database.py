from sqlalchemy import create_engine
from sqlalchemy.orm import Session

from app.core.config import settings


engine = create_engine(
    settings.DB_STR_CONNECTION,
    echo=True if settings.ENVIRONMENT == "development" else False
)


def get_session() -> Session:
    return Session(engine)
