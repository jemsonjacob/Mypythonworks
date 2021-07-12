import re
n=input("enter")
x='[A-Z]{1}[a-z]*$'
match=re.fullmatch(x,n)
if match is not None:
    print("valid")
else:
    print("invalid")