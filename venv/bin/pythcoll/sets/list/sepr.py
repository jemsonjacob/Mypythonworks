s1={1,2,3,4,5,6,7,8,9}
pr=set()
nonpr=set()
for i in s1:
    if i>1:
        for j in range(2,i):
            if(i % j)==0:
                nonpr.add(i)
                break
        else:
              pr.add(i)
print(pr)
print(nonpr)

