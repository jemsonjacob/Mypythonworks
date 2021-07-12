class Add:
    def setval(self,num1,num2):
        self.num1=num1
        self.num2=num2


    def printval(self):
        print(self.num1+self.num2)
ad=Add()
n1=int(input("enter first"))
n2=int(input("enter second"))
ad.setval(n1,n2)
ad.printval()