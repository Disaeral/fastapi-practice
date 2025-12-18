from abc import abstractmethod, ABC
from typing import List, Generic
from type_vars import E, ID


class GenericCRUDRepo(ABC, Generic[E, ID]):
    @abstractmethod
    def get_all(self) -> List[E] | List[None]:
        pass

    @abstractmethod
    def get_by_id(self, id: ID) -> E | None:
        pass

    @abstractmethod
    def create(self, entity: E) -> E:
        pass

    @abstractmethod
    def update(self, entity: E) -> E:
        pass

    @abstractmethod
    def delete(self, id: ID) -> E:
        pass
