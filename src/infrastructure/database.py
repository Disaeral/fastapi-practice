from sqlalchemy import create_engine, text
from sqlalchemy.orm import sessionmaker, Session
from src.core.config import config, Config

class Database:
    
    def __init__(self, config: Config):
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

def init_db() -> Database:
    return Database(config)

db = init_db()
