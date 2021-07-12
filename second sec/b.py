class Bank:
    users = {
        1000: {"acc_no": 1000, "password": "user1", "balance": 3000},
        1001: {"acc_no": 1001, "password": "user2", "balance": 4000},
        1002: {"acc_no": 1002, "password": "user2", "balance": 5000},
        1003: {"acc_no": 1003, "password": "user3", "balance": 6000}
    }
    session = {}

    def validate_account(self, acc_no):
        if acc_no in Bank.users:
            return True
        else:
            return False

    def authenticate(self, **kwargs):
        acc_no = kwargs['acc_no']
        password = kwargs['password']
        user = self.validate_account(acc_no)
        if user:
            if password == self.users[acc_no]['password']:
                self.session['user']=acc_no
                return acc_no
            else:
                return -1
        else:
            print("invalid ac no")
            return 0

    def bal_enq(self, acc_no):
        if (acc_no == self.session['user']):
            print(self.users[acc_no]['balance'])
        else:
            print("you must login")


obj = Bank()
user = obj.authenticate(acc_no=1000, password='user1')
obj.bal_enq(user)

obj1 = Bank()
user = obj1.authenticate(acc_no=1000, password='user1')
obj1.bal_enq(user)
if (user == -1) | (user == 0):
    print("aut fail")
else:
    obj.bal_enq(user)
