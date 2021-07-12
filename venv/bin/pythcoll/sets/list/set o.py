set1={1,2,3,4,5,6,7,8,9,98,78,43,56,25}
o=set()
e=set()
for i in set1:
    if i%2==0:
       e.add(i)
    else:
         o.add(i)
print("even set",e)
print("odd set",o)






