def traingle(n):
    k=n
    for i in range(0,n):
        for r in range(0,k):
         print(end="")
         k=k-1
         print("  ", end="")
        for j in range(n):
            print("* ",end="")
            print("\r")
traingle(5)