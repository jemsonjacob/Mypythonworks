class Person:
    def pvalue(self,name,age):
        self.name = name
        self.age = age
        print(self.name,self.age)

class Parent:
    def paval(self,adrs,phon):
        self.adrs=adrs
        self.phon=phon
        print(self.adrs,self.phon)
class Employe(Person,Parent):
    def eval(self,eid,dept):
        self.eid=eid
        self.dept=dept
        print(self.eid,self.dept)
e=Employe()
e.pvalue("anu",55)
e.paval("arravindaserry",123456)
e.eval(101,"federal")