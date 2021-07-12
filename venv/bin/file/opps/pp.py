class Person:
    def pval(self,name,age):
        self.name = name
        self.age = age
        print(self.name,self.age)
class Child(Person):
    def cval(self,teacher,sub):
        self.teacher=teacher
        self.sub=sub
        print(self.teacher,self.sub)

class Parent(Person):
    def paval(self,adrs,cls):
        self.adrs=adrs
        self.cls=cls
        print(self.adrs,self.cls)

class Student(Child):
    def paval(self,roll,school):
        self.roll=roll
        self.school=school
        print(self.roll,self.school)

e=Person()
e.pval("anu",55)
c=Child()
c.cval("arravin", "plusone")
d=Parent()
d.paval("anu", 44)
f=Student()
f.paval(11,"gvhss")





