from functions import register, login


k = int(input('Sign up/Sign in(0/1)'))
is_registered = False

if k == 0:
    is_registered = register()

if (k == 0 and is_registered) or k == 1:
    users_id = login()
    print(users_id)
else:
    print('User cannot registered! Please try again')
    is_registered = register()

# VCS - Version Control System
