import json


def get_data():
    try:
        with open('users.json', 'r') as f:
            users: list = json.load(f)
            return users
    except (FileNotFoundError, json.JSONDecodeError):
        with open('users.json', 'w') as f:
            json.dump([], f, indent=4)
            return []


class User:

    def __init__(self, first_name, last_name, birth_date, email, username, password):
        self.first_name = first_name
        self.last_name = last_name
        self.birth_date = birth_date
        self.email = email
        self.username = username
        self.__password = password

    def append_to_json(self):
        users = get_data()
        if not self.user_exists():
            user = {
                'id': users[-1]['id'] + 1 if len(users) != 0 else 1,
                'first_name': self.first_name,
                'last_name': self.last_name,
                'birth_date': self.birth_date,
                'email': self.email,
                'username': self.username,
                'password': self.__password,
            }
            users.append(user)
            with open('users.json', 'w') as f:
                json.dump(users, f, indent=4)
            return True
        else:
            return False

    def user_exists(self):
        users: list = get_data()

        for user in users:
            if user['username'] == self.username or user['email'] == self.email:
                return True
        return False
