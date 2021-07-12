class Teach:
    college="Matha"


    def __init__(self, name, subject, department, id):
        self.name = name
        self.subject = subject
        self.department = department
        self.id = id

    def printdetails(self):
        print("name:", self.name)
        print("subject:", self.subject)
        print("department:", self.department)
        print("id:", self.id)
        print("clg",Teach.college)



t=Teach("anu", "biology", "science", 101)
t.printdetails()

