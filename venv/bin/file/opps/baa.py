class Bank:
    def accval(self, name, account_num):
        self.name = name
        self.account_num = account_num
    def bankval(self, deposit, withdraw):
        self.deposit = deposit
        self.withdraw = withdraw
    def balval(self, balance):
        self.balance = balance
        print("balance:", self.balance)


    def depval(self):
      print("deposit into", self.deposit)
      print("balance:", self.balance + self.deposit)


    def withval(self):
      print("widthdraw from", self.withdraw)
      print("balance:", self.balance - self.withdraw)
obj=Bank()
a = input("enter the account number")
obj.accval("anu",a)
obj.balval(20000)
print("1.deposit")
print("2.withdraw")
choice = input("enter the operation")
if choice in ("1", "2"):
     if choice == '1':
            b = int(input("enter amount deposit"))
            obj.bankval(b) 
     elif choice == '2':
           c= int(input("enter amount to withdraw"))
           obj.bankval(c)
else:
   print("invalid")

obj.depval()
obj.withval()