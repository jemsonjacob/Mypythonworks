n=int(input("enter"))

for i in range(1,n):
    print("*" * (n-i),end=" ")
    for j in range(0,i):
        print("*"*(n),end=" ")
    print()