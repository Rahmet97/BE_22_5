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
