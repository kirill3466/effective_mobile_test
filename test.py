import os
import unittest

from lib import Library, Status


class TestLibrary(unittest.TestCase):
    @classmethod
    def setUpClass(cls):
        """создаем библиотеку перед всеми тестами и очищаем"""
        cls.library = Library(path='test_library.json')
        cls.library.books = []

    @classmethod
    def tearDownClass(cls):
        """удаляем файл после всех тестов"""
        if os.path.exists('test_library.json'):
            os.remove('test_library.json')

    def test_add_book(self):
        """добавление книги"""
        self.library.add_book("тестназвание", "теставтор", 2024)
        self.assertEqual(len(self.library.books), 1)
        self.assertEqual(self.library.books[0].title, "тестназвание")
        self.assertEqual(self.library.books[0].author, "теставтор")
        self.assertEqual(self.library.books[0].year, 2024)

    def test_remove_book(self):
        """удаление книги"""
        self.library.add_book("тестназвание", "теставтор", 2024)
        book_id = self.library.books[0].id
        self.library.remove_book(book_id)
        self.assertEqual(len(self.library.books), 0)

    def test_find_book(self):
        self.library.add_book("тестназвание 1", "теставтор", 2024)
        self.library.add_book("тестназвание 2", "другойавтор", 2023)
        self.library.add_book("тестназвание 3", "теставтор", 2024)

        found_books = self.library.find_book("2024")

        self.assertIsNotNone(found_books)
        self.assertEqual(len(found_books), 4)
        self.assertIn(
            found_books[2].title, ["тестназвание 1", "тестназвание 3"]
        )
        self.assertIn(
            found_books[3].title, ["тестназвание 1", "тестназвание 3"]
        )

    def test_change_status(self):
        """изменение статуса"""
        self.library.add_book("тестназвание", "теставтор", 2024)
        self.library.books[0].status = Status.borrowed
        self.assertEqual(self.library.books[0].status, Status.borrowed)


if __name__ == "__main__":
    unittest.main()
