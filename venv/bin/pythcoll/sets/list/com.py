s1={1,2,3,4,5,6}
s2={0,1,8,7,9,3,4}
s3=set()
for i in s1:
    if i in s2:
        s3.add(i)

print(s3)

