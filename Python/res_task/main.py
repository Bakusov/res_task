import random
from faker import Faker
import json
from itertools import count

count_pk = count(1)  # счетчик pk от 1


# получить имя модели из файла conf.py
# [out] str - имя модели
def get_model() -> str:
    with open("conf.py", "r", encoding="UTF-8") as file:
        for line in file:
            if line.find("model = ") != -1:
                return line[len("model = "):]  # возвращаем текст после "model = "
    # если не нашли
    return "shop_final.book"


# сгенерировать имя книги
# [out] str - имя книги
def get_name_book() -> str:
    book_names = []  # список имен книг
    with open("books.txt", "r", encoding="UTF-8") as file:
        for line in file:
            book_names += [line.strip()]
    if len(book_names) == 0:
        # список не может быть пустым, вернем хоть что-то
        return "нет имен"
    # возвращаем случайное имя
    return random.choice(book_names)


# сгенерировать год выпуска книги
# [out] int - год книги  в диапазоне
def get_year() -> int:
    return random.randint(0, 2021)


# сгенерировать кол-во страниц в книге
# [out] int - кол-во страниц
def get_pages() -> int:
    return random.randint(0, 2000)


# сгенерировать международный книжный номер
# [out] str - международный книжный номер
def get_book_id() -> str:
    return Faker().isbn13()


# сгенерировать рейтинг книги
# [out] float - рейтинг книги
def get_rating() -> float:
    return random.randint(0, 500) / 100


# сгенерировать цену за книгу
# [out] float - цена
def get_price() -> float:
    return random.random()


# сгенерировать скидку
# [out] int - скидка от 0 до 90
def get_discount() -> int:
    return random.randint(0, 90)


# сгенерировать авторов
# [in] int=3 - максимальное количество авторов
# [out] list - авторы
def get_authors(max_: int = 3) -> list:
    name_author = []  # список имен авторов
    for _ in range(0, random.randint(1, max_)):
        name_author += [Faker().name()]
    return name_author


# генерация одной книги
# [out] dict - одна книга
def generate_book() -> dict:
    book = {
        "model": get_model(),
        "pk": next(count_pk),
        "fields": {
            "title": get_name_book(),
            "year": get_year(),
            "pages": get_pages(),
            "isbn13": get_book_id(),
            "rating": get_rating(),
            "price": get_price(),
            "discount": get_discount(),
            "author": get_authors()
        }
    }
    #    print(book) # печать сгенерированной книги
    return book


# главная ф-ция - генерация книг и запись в файл
# [in] int - кол-во книг для генерации (по умолчанию 100)
def main(num: int = 100):
    with open("books.json", "w", encoding="UTF-8") as file:
        for _ in range(num):
            json.dump(generate_book(), file, indent=4, ensure_ascii=False)


# тестовая распечатка файла для проверки корректности записи
def print_json_file():
    with open("books.json", "r", encoding="UTF-8") as file:
        for line in file:
            print(line.strip())


if __name__ == '__main__':
    #    print(help(main)) # проверка что help работает
    main()
#    print_json_file()
