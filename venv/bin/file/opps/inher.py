class Person:
    def pdetails(self,name,age,adrs):
        self.name = name
        self.age=age
        self.adrs=adrs
        print(self.name,self.age,self.adrs)
class Emp(Person):
    def edetails(self,id,department,salary):
        self.id=id
        self.department=department
        self.salary=salary
        print(self.name,"id is",self.id)
        print(self.name,"salary is",self.salary)
e=Emp()
e.pdetails("nanuu",55,"muttungal house")
e.edetails(101,"lab",5000)