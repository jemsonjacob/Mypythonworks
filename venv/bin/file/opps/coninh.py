class Employee:
    def __init__(self,eid,ename):
           self.eid=eid
           self.ename=ename
    def printval(self):
        print("id",self.eid)
        print("name",self.ename)
class Parent(Employee):
    def __init__(self,addr,state,eid,ename):
        super().__init__(eid,ename)
        self.addr = addr
        self.state = state
    def print(self):
        print("addrs",self.addr)
        print("state",self.state)

cr=Parent("milunkal","ekm",101,"babu")
cr.printval()
cr.print()
