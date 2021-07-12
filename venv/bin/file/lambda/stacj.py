stk=[]
size=int(input("enter size"))
top=0
n=0
def push():
    global top,size
    if(top>size):
        print("stack full")
    else:
        p=int(input("enter element to push"))
        stk.append(p)
        top+=1
def pop():
    global top,size
    if(top<0):
        print("stack empty")
    else:

        stk.pop()
        top-=1
def display():
    print(stk)
while(n!=1):
    print("enter operation")
    opt=int(input("press 1.push 2.pop 3.display 4.exit"))
    if(opt==1):
        push()
    elif(opt==2):
        pop()
    elif(opt==3):
        display()
    elif(opt==4):
        exit()
n=int(input("do u want to continue press 1 for exit"))
