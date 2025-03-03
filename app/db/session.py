from sqlmodel import create_engine, Session

from app.core.config import settings


engine = create_engine(settings.database_url)

# Dependency funxtion to get a session
def get_session() -> Session:
    session = Session(bind=engine)
    try:
        yield session
    finally:
        session.close()