def check(func):
    def wrapper(name,age):
        if age<18:
            print("not eligible")
        else:
            return func(name,age)
    return wrapper    

@check
def vacccine(name,age):
    print(name,"eligible")
vacccine("anu",45)