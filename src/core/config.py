from pydantic_settings import BaseSettings, SettingsConfigDict
from pydantic import computed_field
from functools import lru_cache
from os import getenv
from dotenv import load_dotenv

load_dotenv()

class Config(BaseSettings):
    PORT: int = int(getenv("PORT", 8000))
    HOST: str = getenv("HOST", "localhost")
    ENVIRONMENT: str = getenv("ENVIRONMENT", "LOCAL")
    PG_DB_DRIVER: str = getenv("PG_DB_DRIVER", "postgres")
    PG_DB_NAME: str = getenv("PG_DB_NAME", "postgres")
    PG_DB_USER: str = getenv("PG_DB_USER", "postgres")
    PG_DB_PASSWORD: str = getenv("PG_DB_PASSWORD", "")
    PG_DB_HOST: str = getenv("PG_DB_HOST", "localhost")
    PG_DB_PORT: int = int(getenv("PG_DB_PORT", 5432))
    MYSQL_DB_DRIVER: str = getenv("MYSQL_DB_DRIVER", "mysql")
    MYSQL_DB_NAME: str = getenv("MYSQL_DB_NAME", "mysql")
    MYSQL_DB_USER: str = getenv("MYSQL_DB_USER", "mysql")
    MYSQL_DB_PASSWORD: str = getenv("MYSQL_DB_PASSWORD", "")
    MYSQL_DB_HOST: str = getenv("MYSQL_DB_HOST", "localhost")
    MYSQL_DB_PORT: int = int(getenv("MYSQL_DB_PORT" , 3306))
    DB_POOL_SIZE: int = 20
    DB_MAX_OVERFLOW: int = 10
    DB_POOL_PRE_PING: bool = True
    DB_POOL_RECYCLE: int = 1800
    DB_ECHO: bool = bool(getenv("DB_ECHO", False))

    @computed_field
    @property
    def url(self) -> str:
        from sqlalchemy import URL
        return URL.create(
            drivername=self.PG_DB_DRIVER,
            username=self.PG_DB_USER,
            password=self.PG_DB_PASSWORD,
            host=self.PG_DB_HOST,
            database=self.PG_DB_NAME,
        ).render_as_string(hide_password=False)

class DevelopmentConfig(Config):
    PORT: int = 8221
    ENVIRONMENT: str = "DEVELOPMENT"

class LocalConfig(Config):
    ENVIRONMENT: str = "LOCAL"

class ProductionConfig(Config):
    ENVIRONMENT: str = "PRODUCTION"

@lru_cache()
def get_config():
    env = getenv("ENVIRONMENT", "LOCAL")
    config_type = {
        "DEVELOPMENT": DevelopmentConfig(),
        "LOCAL": LocalConfig(),
        "PRODUCTION": ProductionConfig(),
    }
    return config_type[env]

config = get_config()
