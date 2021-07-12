x = input("enter the string")
count = 0
for i in x:
    count = x.count(i)
    if count > 1:
        break
print("first" ,i)
