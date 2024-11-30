# effective_mobile_test

Это простое приложение для управления библиотечной коллекцией. Оно позволяет добавлять, удалять, искать книги, а также изменять их статус. Данные о книгах хранятся в JSON файле.

## Функциональность

Добавление книги: Пользователь может добавить новую книгу, указав её название, автора и год издания.
Удаление книги: Пользователь может удалить книгу по её идентификатору (ID).
Поиск книг: Пользователь может искать книги по названию, автору или году издания.
Изменение статуса книги: Пользователь может изменить статус книги (например, с "в наличии" на "выдана").
Просмотр всех книг: Пользователь может просмотреть список всех книг в библиотеке.
Запуск тестов: Пользователь может запустить тесты для проверки функциональности приложения.
## Установка и запуск
```
git clone https://github.com/kirill3466/effective_mobile_test.git
python main.py
```
## Структура проекта
books.json: Файл, в котором хранятся данные о книгах.
lib.py: Основной модуль с классом Library для управления книгами.
main.py: Основной скрипт для запуска приложения и взаимодействия с пользователем.
schema.py: Модуль с классами данных и перечислениями для описания книг и их статусов.
test.py: Модуль с тестами для проверки функциональности приложения.
Тестирование
