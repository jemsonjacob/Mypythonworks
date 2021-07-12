def pat(n):
 for i in range(0,n):
  print("*",n-i)
  for j in range(n-i):

    print(" * ", end=" ")
print("")
pat(3)