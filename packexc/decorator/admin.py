def admin_required(func):
    def wrapper(user,pin):
        if user!='admin':
            raise Exception("no authority")
        else:
          return func(user,pin)

    return wrapper
@admin_required
def change_pin(user,pin):
    mypin=pin
    return mypin
def delete_ac(user,acno):
    return str(acno)+"delete"
print(change_pin("admin",1000))
