import os

from lib import Library
from test import TestLibrary
from unittest import TestLoader, TextTestRunner


def clear_console():
    """очищает консоль"""
    os.system('cls' if os.name == 'nt' else 'clear')


def menu():
    print("*" * 20)
    print("*" * 4, "Библиотека", "*" * 4)
    print("*" * 20)


def run_tests():
    """запускает тесты"""
    clear_console()
    print("запуск тестов...")
    loader = TestLoader()
    suite = loader.loadTestsFromTestCase(TestLibrary)
    runner = TextTestRunner()
    runner.run(suite)
    input("\nНажмите Enter для продолжения...")


def main():
    lib = Library()

    while True:
        clear_console()
        menu()
        print("1 - Добавить книгу")
        print("2 - Удалить книгу")
        print("3 - Найти книги")
        print("4 - Изменить статус книги")
        print("5 - Показать все книги")
        print("6 - Запустить тесты")
        print("7 - Выход\n")

        choice = input("выберите действие: ")

        try:
            if choice == '1':
                title = input("введите название книги: ")
                author = input("введите имя автора: ")
                year = int(input("введите год издания: "))
                lib.add_book(title, author, year)

            elif choice == '2':
                book_id = int(input("введите id книги для удаления: "))
                lib.remove_book(book_id)

            elif choice == '3':
                query = input(
                    "введите название книги автора или год для поиска: "
                )
                lib.find_book(query)

            elif choice == '4':
                book_id = int(input(
                    "введите id книги для изменения статуса: ")
                )
                lib.change_status(book_id)

            elif choice == '5':
                lib.all_books()

            elif choice == '6':
                run_tests()

            elif choice == '7':
                break

            else:
                print("некорректный выбор")

        except ValueError as e:
            print(f"ошибка: {e}")
            print("некорректные данные")

        input("\nНажмите Enter для продолжения...")


if __name__ == "__main__":
    main()
