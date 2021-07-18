import json
from csv import DictReader

# парсим список книг и пересоздаем с нужными полями
books_list = []
with open("books.csv", "r") as file:
    reader = DictReader(file)

    for row in reader:
        books_list.append({
            "title": row["Title"],
            "author": row["Author"],
            "pages": row["Pages"],
            "genre": row["Genre"]
        })

# парсим список пользователей и пересоздаем с нужными полями
users_list = []
with open("users.json", "r") as f:
    json_users = json.loads(f.read())
    for json_user in json_users:
        users_list.append({
            "name": json_user['name'],
            "gender": json_user['gender'],
            "address": json_user['address'],
            "age": json_user['age'],
            "books": []
        })

# раздаем последовательно книги каждому пользователю
while len(books_list) > 0:
    for user in users_list:
        if len(books_list) > 0:
            user["books"].append(books_list.pop(0))
        else:
            break
else:
    del books_list

# записываем результаты в result.json
with open("result.json", "w") as f:
    s = json.dumps(users_list, indent=4)
    f.write(s)
