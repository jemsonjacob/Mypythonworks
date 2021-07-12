def check(func):
    def wrapper(num1,num2):
        if num1<num2:
            temp=num1
            num1=num2
            num2=temp

            return func(num1,num2)

    return wrapper


@check
def sub(num1,num2):
    return num1-num2
print(sub(2,10))