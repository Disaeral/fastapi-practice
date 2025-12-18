from abc import ABC, abstractmethod
from typing import Generic, TypeVar


E = TypeVar("E")  # e for entity
ID = TypeVar("ID")
ORM = TypeVar("ORM")

class Mapper(ABC, Generic[E, ORM]):
    @staticmethod
    @abstractmethod
    def _to_domain(orm: ORM) -> E:
        pass
    @staticmethod
    @abstractmethod
    def _to_orm(e: E) -> ORM:
        pass