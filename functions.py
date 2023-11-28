import json
from datetime import datetime

from users import User, get_data


def register():
    first_name = input('Enter your first name: ')
    last_name = input('Enter your last name: ')
    birth_date = input('Enter your birth date: ')
    email = input('Enter your email: ')
    username = input('Enter your username: ')
    password = input('Enter your password: ')

    user = User(first_name, last_name, birth_date, email, username, password)
    return user.append_to_json()


def login():
    username = input('Enter your username: ')
    password = input('Enter your password: ')

    users = get_data()

    for user in users:
        if user['username'] == username and user['password'] == password:
            return user['id']
    return 0


def add_to_shopping_cart(movie_id, user_id, count=1):
    with open('shopping_cart.json') as f:
        movies = json.load(f)
        f.close()
    movie = {
        'id': 1 if len(movies) == 0 else movies[-1]['id'] + 1,
        'movie_id': movie_id,
        'user_id': user_id,
        'count': count,
        'created_date': str(datetime.now())
    }
    movies.append(movie)
    with open('shopping_cart.json', 'w') as f:
        json.dump(movies, f, indent=4)
        f.close()
