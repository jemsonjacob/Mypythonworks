class Parent:
    def printval(self,name):
        self.name=name

        print("inside parent",self,name)

class Child(Parent):
    def printval(self,class1):
        self.class1=class1
        print("inside child method",self.class1)
ch=Child()
ch.printval("abc")