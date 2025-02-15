from sqlmodel import create_engine, Session
from app.core.config import settings


engine = create_engine(settings.database_url)

def get_session() -> Session:
    with Session(engine) as session:
        yield session