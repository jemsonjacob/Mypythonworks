import re

f = open('numbers', 'r')
f1 = open('valid', 'w')
for i in f:
    i=i.strip()
    x = '([K][L]\d{2}[A-Z]{2}\d{4}$)'
    match = re.fullmatch(x,i)
    if match is not None:
     f1.write(i)
     f1.write("\n")