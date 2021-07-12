class Operator:
    def num(self,n1,n2,n5):
        self.n1=n1
        self.n2=n2
        self.n5=n5
        print(self.n1+self.n2+self.n5)
class Display(Operator):
    def num1(self,n3,n4):
     self.n3=n3
     self.n4=n4
     print(self.n3-self.n4)
di=Display()
di.num(3)
