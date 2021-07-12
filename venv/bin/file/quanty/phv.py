import re
f=open("phon",'r')
f1=open("pp",'w')
x='[+][9][1]\d{10}'
for i in f:
    i=i.strip()
    match=re.fullmatch(x,i)
    if match is not None:
        f1.write(i)
        f1.write("\n")