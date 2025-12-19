from src.core.mappers import Mapper
from src.infrastructure.entities.user import User as UserORM
from src.core.entities.user import User

class UserMapper(Mapper):
    @staticmethod
    def _to_domain(orm: UserORM) -> User:
        return User(username=orm.username, password=orm.password, fullname=orm.fullname, is_banned=orm.is_banned)
    @staticmethod
    def _to_orm(e: User) -> UserORM:
        return UserORM(username=e.username, password=e.password, fullname=e.fullname, is_banned = e.is_banned)