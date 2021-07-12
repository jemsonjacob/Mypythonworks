class Student:
    school="matha college"
    def setval(self,name,age,mark):
        self.name=name
        self.age = age
        self.mark = mark

    def printval(self):
        print("name::",self.name)
        print("age::", self.age)
        print("mark::", self.mark)
        print(Student.school)

stu=Student()
n=input("enter name")
a=int(input("age"))
m=int(input("marks"))

stu.setval(n,a,m)
stu.printval()