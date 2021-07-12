def authenticate(user, password):
    if user in users:
        if (password ==users[user]['password']):
            print("Succes")
        else:
            print("invalid")
def get_bal(accno):
    if accno in users:
        print(users[accno]['balance'])
    else:
        print("invalid")
get_bal(1000)        