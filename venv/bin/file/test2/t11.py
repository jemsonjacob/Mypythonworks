import re
n=input("enter")
x='^[a]{1}\d*[b]$'
match=re.fullmatch(x,n)
if match is not None:
    print("valid")
else:
    print("invalid")