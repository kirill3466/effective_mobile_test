from dataclasses import dataclass
from enum import Enum
from typing import List


class Status(Enum):
    available = "в наличии"
    borrowed = "выдана"


@dataclass
class Book:
    id: int
    title: str
    author: str
    year: int
    status: Status

    def to_dict(self):
        return {
            'id': self.id,
            'title': self.title,
            'author': self.author,
            'year': self.year,
            'status': self.status.value
        }


@dataclass
class BookList:
    books: List[Book]
