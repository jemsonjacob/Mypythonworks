class Student:
 def __init__(self,name,roll,dept,mark):
     self.name=name
     self.roll=roll
     self.dept=dept
     self.mark=mark
 def pval(self):
     print("name",self.name)
     print("roll",self.roll)
     print("depart",self.dept)
     print("mark",self.mark)
def __str__(self):
    return self.name
f=open('tfile','r')
for i in f:
    data=i.rstrip("\n").split(",")
    name=data[0]
    roll=data[1]
    dept=data[2]
    mark=data[3]
    o=Student(name,roll,dept,mark)
    print(o)
    o.pval()
