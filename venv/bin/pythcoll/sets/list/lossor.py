ls=[100,-44,5,0,66]
temp=list()
for i in ls:
   if i>i+1:
      for j in ls:
       temp.append(i)
print(temp)
