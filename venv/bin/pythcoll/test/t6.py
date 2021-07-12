def pri(n):
    sum=0
    if n > 1:
       for i in range(1,50):
           for i in range(2, n):
                if (n % i) == 0:
                    sum=sum+i
                return(sum)

print(sum)
