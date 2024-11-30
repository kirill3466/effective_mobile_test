import json
from typing import Optional, Union

from schema import Book, BookList, Status

PATH = 'books.json'


class Library:
    def __init__(self, path: Optional[str] = None):
        self.path = path or PATH
        self.books = self.load_books()

    def load_books(self) -> BookList:
        """Считывает книги из JSON файла

        Returns:
            BookList: Список объектов Book

        Raises:
            FileNotFoundError: Если файл не найден, он будет создан и
            вернет пустой список
        """
        try:
            with open(self.path, 'r', encoding='utf-8') as file:
                books = json.load(file)
                return [
                    Book(
                        **{**book, 'status': Status(book['status'])}
                    ) for book in books
                ]
        except FileNotFoundError:
            with open(self.path, 'w', encoding='utf-8') as file:
                json.dump([], file, ensure_ascii=False, indent=4)
            print(f"Файл {self.path} был создан.")
            return []

    def save_books(self) -> None:
        """Сохраняет книги в JSON файл"""
        with open(self.path, 'w', encoding='utf-8') as file:
            json.dump(
                [book.to_dict() for book in self.books],
                file,
                ensure_ascii=False,
                indent=4
            )

    def add_book(self, title: str, author: str, year: int) -> None:
        """Добавляет новую книгу в библиотеку

        Args:
            title (str): название книги
            author (str): автор книги
            year (int): год публикации книги
        """
        if not title or not author or not year:
            print("\nне все поля заполнены")
            return
        if self.books:
            new_id = max(book.id for book in self.books) + 1
        new_id = 1
        new_book = Book(
            id=new_id,
            title=title,
            author=author,
            year=year,
            status=Status.available
        )
        self.books.append(new_book)
        self.save_books()
        print(f"\nкнига '{title}' добавлена, id - {new_id}")

    def remove_book(self, book_id: int) -> None:
        """Удаляет книгу с указанным id

        Args:
            book_id (int): id книги для удаления
        """
        if not book_id:
            print("\nзаполните id")
            return
        if book_id not in [book.id for book in self.books]:
            print(f"\nкнига с id {book_id} не найдена")
            return
        self.books = [book for book in self.books if book.id != book_id]
        self.save_books()
        print(f"\nкнига с id {book_id} удалена")

    def find_book(self, query: str) -> Union[list[Book], None]:
        """Ищет книги по запросу

        Args:
            query (str): Запрос для поиска (название, автор или год)

        Returns:
            Union[list[Book], None]: Список найденных книг или None
        """
        if not query:
            print("\nзаполните запрос")
            return
        found_books = [
            book for book in self.books if (query in book.title)
            or (query in book.author)
            or (query in str(book.year))
        ]
        if found_books:
            print("\nнайденные книги:")
            for book in found_books:
                status = Status(book.status)
                print(f"{book.id}: '{book.title}' - автора {book.author}, год - {book.year} ({status.value})")
        else:
            print("\nбиблиотека пуста или ничего не найдено")
        return found_books

    def change_status(self, book_id: int) -> None:
        """Изменяет статус книги

        Args:
            book_id (int): id книги
        """
        if not book_id:
            print("\nзаполните id")
            return
        if book_id not in [book.id for book in self.books]:
            print(f"\nкнига с id {book_id} не найдена")
            return
        new_status = input("введите новый статус (в наличии или выдана): ")
        if not new_status:
            print("\nзаполните статус")
            return
        try:
            new_status = Status(new_status)
        except ValueError:
            print("\nнеправильно указан статус")
            return
        for book in self.books:
            if book.id == book_id:
                book.status = new_status
                self.save_books()
                print(
                    f"\nуспешно изменен статус книги с id {book_id} на {new_status.value}"
                    )
                return
        print(f"\nкнига с id {book_id} не найдена")

    def all_books(self) -> None:
        """Выводит все книги"""
        if self.books:
            print("\nвсе книги: ")
            for book in self.books:
                print(
                    f"{book.id}: '{book.title}' - автора {book.author}, год - {book.year} ({book.status.value})"
                )
        else:
            print("\nнет книг")
