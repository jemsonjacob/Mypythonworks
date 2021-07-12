class Person:
    def pval(self,name,age):
        self.name = name
        self.age = age
        print(self.name,self.age)
class Parent(Person):
    def paval(self,adrs,cls):
        self.adrs=adrs
        self.cls=cls
        print(self.adrs,self.cls)
class Employee(Parent):
    def eval(self,eid,dept):
        self.eid=eid
        self.dept=dept
        print(self.eid,self.dept)

ch=Parent()
ch.paval("arravin","plusone")
ch.pval("anu",44)

st=Employee()
st.eval(101,"fire")
st.paval("mukul","ten")
st.pval("manu",55)
