import re

n=input("enter")
x='^[k][l][4][2]\d{4}$'
match=re.fullmatch(x,n)
if match is not None:
    print("valid")
else:
    print("not valid")
