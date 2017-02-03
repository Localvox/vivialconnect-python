from vivialconnect import User


def list_users():
    users = User.find()
    for user in users:
        print(user.id, user.first_name, user.last_name)


def get_user(id):
    user = User.find(id)
    print(user.id, user.first_name, user.last_name)


def update_user(id, first_name=None, last_name=None):
    user = User.find(id)
    user.first_name = first_name
    user.last_name = last_name
    user.save()
