import datetime
import json

from functions import register, login, add_to_shopping_cart
from utils import print_tab

k = int(input('Sign up/Sign in(0/1)'))
is_registered = False
user_id = 0

if k == 0:
    is_registered = register()

if (k == 0 and is_registered) or k == 1:
    user_id = login()
else:
    print('User cannot registered! Please try again')
    is_registered = register()
    user_id = login()

p = int(input("0: Exit, 1: Show movies = "))

if p == 0 and user_id != 0:
    pass
elif p == 1 and user_id != 0:
    with open('movie.json', 'r') as f:
        movies = json.load(f)
        print_tab(movies)
        movie_id = int(input("Enter movie ID to like it: "))
        with open('likes.json') as f1:
            likes = json.load(f1)
            f1.close()
        like = {
            'id': 1 if len(likes) == 0 else likes[-1]['id'] + 1,
            'user_id': user_id,
            'movie_id': movie_id,
            'liked_at': str(datetime.datetime.now())
        }
        likes.append(like)
        with open('likes.json', 'w') as f1:
            json.dump(likes, f1, indent=4)
            print('Congratulations :)')
            f1.close()

        p = int(input("0: Exit, 1: Add to shopping cart  "))
        if p == 0 and user_id !=0:
            pass
        elif p == 1 and user_id != 0:
            add_to_shopping_cart(movie_id, user_id)
