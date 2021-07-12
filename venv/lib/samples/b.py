def traingle(n): 
    k = n
    for i in range(0,n):
        for r in range(0,k):
            print(end=" ")
        k=k-1
        for j in range(0, i+5):
         print("* ",end="")
        print("\r")
traingle(5)
