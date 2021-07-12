a=[1,2,3,4,5]
b=int(input("enter the number "))
try:
    print(a[b])
except Exception as e:
    print("exception occured",e)
