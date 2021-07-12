import re
n=open('fil','r')
f1=open('go','w')
x='[L][U][M]\d{2}[P][Y]\d{3}'
for num in n:
     number= num.rstrip('\n')
     match=re.fullmatch(x,number)
     if match!=None:
         f1.write(num)
         f1.write("\n")