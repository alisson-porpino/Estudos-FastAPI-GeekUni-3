from pydantic_settings import BaseSettings


class Settings(BaseSettings):
    API_V1_STR: str = '/api/v1'
    #DB_URL: str = 'sqlite+aiosqlite:///./teste.db/'
    DB_URL: str = 'postgresql+asyncpg://postgres:1212@localhost:5432/srs'
    #DBBaseModel: DeclarativeMeta = declarative_base()

    class config:
        case_sensitive = True


settings: Settings = Settings()
