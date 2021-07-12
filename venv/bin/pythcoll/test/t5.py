def add(x, y):
    return(x + y)
def sub(x, y):
    return(x - y)
def mul(x, y):
    return (x * y)
def div(x, y):
    return (x / y)
def flor(x, y):
    return (x // y)
def exp(x, y):
    return(x ** y)

print("enter operation")
print("1.add")
print("2.sub")
print("3.mul")
print("4.div")
print("5.floor div")
print("6.exponent")
while True:
    c = int(input("enter choice"))
    if c in ("1", "2", "3", "4", "5", "6"):
        n1 = float(input("enter first num"))
        n2 = float(input("enter second num"))
       if c=="1":
           print(add(n1, n2))
          elif c=="2":
          print(sub(n1, n2)
          elif c=="3":
         print(mul(n1, n2))
           elif c == "4":
          print(div(n1, n2))
       elif c == "5":
        print(flor(n1, n2))
       elif c == 6:
        print(exp(n1, n2)
        break
       else:
              print("invalid chioce")
