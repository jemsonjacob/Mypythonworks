class Calc:
    def __init__(self,a,b):
        self.a = a
        self.b = b

    def add(self):
      return self.a+self.b

    def sub(self):
        return self.a - self.b

    def mul(self):
        return self.a * self.b

    def div(self):
      return self.a/self.b

a=int(input("first"))
b=int(input("second"))
ca = Calc(a,b)
print(ca.add())
print(ca.sub())
print(ca.mul())
print(ca.div())
