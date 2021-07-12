class Bank:
    users = {
        1000: {"acconum": 1000, "password": "user1", "balance": 3000},
        1001: {"acconum": 1001, "password": "user2", "balance": 4000},
        1002: {"acconum": 1002, "password": "user3", "balance": 5000},
        1003: {"acconum": 1003, "password": "user4", "balance": 6000}}

    session = {}

    def validate(self, accno):
        if accno in self.users:
            return True
        else:
            return False

    def authenticate(self, **kwargs):
        acc_no = kwargs["acc_no"]
        password = kwargs["password"]
        user = self.validate(acc_no)
        if user:
            if password == self.users[acc_no]["password"]:
                self.session["users"] = acc_no
                return acc_no
            else:
                return -1
        else:
            return 0

    def balance_enquiry(self, acc_no):
        if(acc_no == self.session["users"]):
            balance=self.users[acc_no]['balance']
            print(self.users[acc_no]["balance"])

        else:
            print("invalid password")

    def fund_transfer(self, user, to_acc, amount):
        if self.validate(to_acc):
            balance = self.users[user]['balance']
            if balance < amount:
                print("insuff")
            else:
                self.users[user]['balance'] -= amount
                self.users[to_acc]['balance'] += amount


obj = Bank()
user = obj.authenticate(acc_no=1000, password="user1")
obj.balance_enquiry(user)

obj1 = Bank()
user = obj1.authenticate(acc_no=1001, password="user2")
if user == -1 or user == 0:
    print("invalid details")
else:
    obj1.balance_enquiry(user)
obj.fund_transfer(user, 1000, 500)
obj1.balance_enquiry(user)
