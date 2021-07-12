class Bank:
    def setval(self,accno):
        self.accno=accno

    def bankval(self,deposit,withdraw):
        self.deposit=deposit
        self.withdraw=withdraw
    def balval(self,balance,name):
        self.balance=balance
        self.name = name
        print("balance:",self.balance)
        print("Name:", self.name)
    def depval(self):
        print("deposit into account number:",self.accno)
        print("balance:",self.balance+self.deposit)
    def withval(self):
        print("widthdraw from account number:", self.accno)
        print("balance:", self.balance - self.withdraw)

obj=Bank()
a=int(input("enter acc no"))
obj.setval(a)
obj.balval(20000,"Anu")
b=int(input("enter amount to deposit"))
c=int(input("enter amount to withdraw"))
obj.bankval(b,c)
obj.depval()
obj.withval()