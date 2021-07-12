class Student:
    def __init__(self, name, roll, clas, mark):
        self.name = name
        self.roll = roll
        self.clas = clas
        self.mark = mark

    def printval(self):
        print("name",self.name)
        print("roll",self.roll)
        print("class",self.clas)
        print("mark",self.mark)

f = open("stu", "r")
for i in f:
     data = i.rstrip("\n").split("\r")
     name = data[0]
     roll = data[1]
     clas = data[2]
     mark = data[3]
     obj = Student(name, roll, clas, mark)

     obj.printval()
