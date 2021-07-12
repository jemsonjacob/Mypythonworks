class Person:
    def __init__(self,name,age):
        self.name = name
        self.age = age
    def pval(self):
        print("name",self.name)
        print("age",self.age)
class Employee(Person):
    def __init__(self,eid,e_company,name,age):
        super().__init__(name,age)
        self.eid=eid
        self.e_company=e_company
    def print(self):
        print(self.eid)
        print(self.e_company)
e=Employee(101,'tata','anoop',25)
e.pval()
e.print()