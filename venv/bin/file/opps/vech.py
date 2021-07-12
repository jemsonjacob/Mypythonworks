class Vechi:
    def inval(self,name,model,company,color):
        self.name = name
        self.model=model
        self.company=company
        self.color=color
    def printval(self):
        print(self.name)
        print(self.model)
        print(self.company)
        print(self.color)
class Bus(Vechi):
    def gotval(self,reg,place):
        self.reg=reg
        self.place=place
        print(self.reg)
        print(self.place)

obj=Vechi()
obj.inval("swift",1900,"benz","green")
obj.printval()
ob=Bus()
ob.gotval("kl43","narakal")
