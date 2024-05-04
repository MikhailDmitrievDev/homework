import json
from abc import ABC, abstractmethod


class Storage(ABC):
    @abstractmethod
    def read(self):
        raise NotImplementedError

    @abstractmethod
    def save(self):
        raise NotImplementedError


class JSONStorage(Storage):
    """Напиши комментарий"""

    async def read(self):
        # TODO Метод не работает...
        with open('data.json') as file:
            return json.load(file)

    def save(self):
        ...
