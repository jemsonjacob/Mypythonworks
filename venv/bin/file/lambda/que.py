q=[]
size=int(input("enter the size of q"))
front=0
n=0
def enq():
    global front,size
    if(front>size):
        print("q is full")
    else:
        p=int(input("enter element to be insert"))
        q.append(p)
        front+=1
def deque():
    global front,size
    if(front<=0):
        print("que is empty")
    else:
     q.pop(0)
     front-=1
def display():
    print(q)
while(n!=1):
    print("enter operation")
    opt=int(input("press 1.enqueue 2.dequeue 3.display 4.exit"))
    if(opt==1):
        enq()
    elif(opt==2):
        deque()
    elif(opt==3):
        display()
    elif(opt==4):
        exit()
n=int(input("do u want to continue press 1 for exit"))
