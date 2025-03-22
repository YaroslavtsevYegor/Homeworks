import csv
import json


def read_users(file):
    """
    Чтение json файла и выделение нужных ключей
    """
    with open(file, 'r') as file_users:
        users = json.load(file_users)
        users_list = []
        for user in users:
            field = {
                'name': user['name'],
                'gender': user['gender'],
                'address': user['address'],
                'age': user['age'],
                'books': []
            }
            users_list.append(field)
    return users_list


def read_books(file):
    """
    Чтение csv файла и выделение нужных столбцов
    """
    with open(file, 'r') as file_books:
        books = csv.DictReader(file_books)
        books_list = []
        for book in books:
            field = {
                'title': book['Title'],
                'author': book['Author'],
                'pages': book['Pages'],
                'genre': book['Genre'],
            }
            books_list.append(field)
    return books_list


def distribute_books(books, users):
    """
    Распределение книг по пользователям и запись в json файл
    """
    books_num = len(books)
    users_num = len(users)
    base_count = books_num // users_num
    extra_count = books_num % users_num
    for i, user in enumerate(users):
        user['books'] = books[i * base_count: (i + 1) * base_count]
        if i < extra_count:
            user['books'].append(books[users_num * base_count + i])
    with open('result.json', mode='w', encoding='utf-8') as result_file:
        json.dump(users, result_file, indent=4)


if __name__ == '__main__':
    books = read_books('books.csv')
    users = read_users('user.json')
    distribute_books(books, users)
