class Employ:
    def setval(self, name, id, salary, age):
        self.name = name
        self.id = id
        self.salary = salary
        self.age = age

    def printval(self):
        print("name::", self.name)
        print("id::", self.id)
        print("salary::", self.salary)
        print("age::", self.age)


pe = Employ()
pe.setval('ajay')
pe.setval('101')
pe.setval('20000')
pe.setval('30')
pe.printval()
