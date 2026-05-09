from dishka import Provider, provide, Scope
from .database import Database
from src.core.config import config
from src.infrastructure.repositories import SQLAlchemyUserRepository
from src.infrastructure.services import FastAPIUserService


class ApiAppProvider(Provider):
    scope = Scope.REQUEST

    @provide
    def get_db(self) -> Database:
        return Database(config)

    @provide
    def get_user_repo(self, db: Database) -> SQLAlchemyUserRepository:
        return SQLAlchemyUserRepository(db.get_session)

    @provide
    def get_user_service(self, repo: SQLAlchemyUserRepository) -> FastAPIUserService:
        return FastAPIUserService(repo)
