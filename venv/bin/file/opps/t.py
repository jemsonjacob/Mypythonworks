class Employee:
    company_name="tata ltd"
    def __init__(self,ename,exp):
        self.ename=ename
        self.exp=exp
    def printdet(self,):
        print("emp name",self.ename)
        print("experience",self.exp)
        print("company",Employee.company_name)
    def __str__(self):
        return str(self.exp)+self.ename
ob=Employee("anu",4)
print(ob)
