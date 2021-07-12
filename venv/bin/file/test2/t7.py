import re
f=open('phone','r')
x='[+][9][1]\d{10}'
for i in f:
    num=i.rstrip('\n')
    matcher=re.fullmatch(x,num)
    if matcher is not None:
      print(num)
