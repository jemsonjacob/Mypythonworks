class Vechicle:
    def vval(self,model,reg_no,color,company):
        self.model=model
        self.reg_no=reg_no
        self.color=color
        self.company=company
    def printval(self):
        print("model-",self.model)
        print("reg_no-", self.reg_no)
        print("color-", self.color)
        print("company-", self.company)

c=Vechicle()
c.vval("e class","kl-42 5050","green","Benz")
c.printval()
print(c)