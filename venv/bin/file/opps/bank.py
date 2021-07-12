class Bank:
    def accval(self, name, account_num, amount):
        self.name = name
        self.account_num = account_num
        self.amount = amount

    def credit(self, account_num, amount, balence):
        self.account_num = account_num
        self.amount = amount
        self.balence = balence
        print("account_number:", self.account_num)
        print("amount:", self.amount)
        print("balence::", cd)

    def debit(self, balence, amount):
        self.amount = amount
        self.balence = balence
        print("amount::", self)
        print("balence::", cw)


n = input("enter the account number")
print("1.deposit")
print("2.withdraw")
choice = input("enter the operation")
if choice in ("1", "2"):
    if choice == '1':
        cd = int(input("enter amount deposit"))
        print("balence=", 20000 + cd)
    elif choice == '2':
        cw = int(input("enter amount to withdraw"))
        print("balence::", 20000 - cw)
else:
    print("invalid")
am = Bank()
am.accval(n,20000,)
am.credit(n, 20000, cd)
am.debit(20000 - cw, 20000)
am.accval()
am.credit()
am.debit()
