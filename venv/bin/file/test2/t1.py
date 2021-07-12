class Vec:
    def vval(self,model,company,year):
        self.model=model
        self.company=company
        self.year=year
    def pval(self):
        print(self.model,self.company,self.year)

class  Bus(Vec):
    def bval(self,reg,color):
        self.reg=reg
        self.color=color

    def bpval(self):
        print(self.reg,self.color)
        print(self.model,self.company,self.year)

o=Bus()
o.bval('kl42-8989','black')
o.vval('swift','maruti',1998)
print(o.bpval())
