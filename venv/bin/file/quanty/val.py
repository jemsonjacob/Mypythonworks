import re

n = input("enter the string")
x = '(^a[a-zA-z0-9\W]*b$)'
match = re.fullmatch(x, n)
if match is not None:
    print("valid")
else:
    print("invalid")
