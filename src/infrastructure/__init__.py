from sqlalchemy import create_engine, text
from sqlalchemy.orm import sessionmaker, Session
from pydantic import Field
from pydantic_settings import BaseSettings

class DatabaseConfig(BaseSettings):
    DB_DRIVER: str = "postgresql+psycopg2"
    DB_USER: str = Field(default="postgres", validation_alias="PG_DB_USER")
    DB_PASSWORD: str = Field(default="", validation_alias="PG_DB_PASSWORD")
    DB_HOST: str = Field(default="localhost", validation_alias="PG_DB_HOST")
    DB_NAME: str = Field(default="postgres", validation_alias="PG_DB_NAME")
    DB_POOL_SIZE: int = 20
    DB_MAX_OVERFLOW: int = 10
    DB_POOL_PRE_PING: bool = True
    DB_POOL_RECYCLE: int = 1800
    DB_ECHO: bool = False
    
    @property
    def url(self) -> str:
        from sqlalchemy import URL
        return URL.create(
            drivername=self.DB_DRIVER,
            username=self.DB_USER,
            password=self.DB_PASSWORD,
            host=self.DB_HOST,
            database=self.DB_NAME,
        ).render_as_string(hide_password=False)

class Database:
    
    def __init__(self, config: DatabaseConfig):
        self.config = config
        self._engine = None
        self._session_factory = None
    
    @property
    def engine(self):
        if self._engine is None:
            self._engine = create_engine(
                self.config.url,
                echo=self.config.DB_ECHO,
                pool_size=self.config.DB_POOL_SIZE,
                max_overflow=self.config.DB_MAX_OVERFLOW,
                pool_pre_ping=self.config.DB_POOL_PRE_PING,
                pool_recycle=self.config.DB_POOL_RECYCLE,
                pool_timeout=30,
                connect_args={
                    "connect_timeout": 10,
                    "application_name": "my_fastapi_app",
                },
            )
        return self._engine
    
    @property
    def session_factory(self):
        """Lazy initialization of session factory"""
        if self._session_factory is None:
            self._session_factory = sessionmaker(
                bind=self.engine,
                class_=Session,
                expire_on_commit=False,
                autocommit=False,
                autoflush=False,
            )
        return self._session_factory
    
    def get_session(self) -> Session:
        return self.session_factory()
    
    async def connect(self):
        with self.engine.connect() as conn:
            conn.execute(text("SELECT 1"))
    
    async def disconnect(self):
        if self._engine:
            self._engine.dispose()
            self._engine = None
            self._session_factory = None