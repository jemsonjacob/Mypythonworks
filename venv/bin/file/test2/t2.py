class College:
    college_name="St.mary's"
    def __init__(self,place,rank):
        self.place = place
        self.rank=rank
        print(self.rank,self.college_name,self.place)

class Teacher(College):
    def __init__(self,t_name,t_dep,t_phone,place,rank):
        super().__init__(place,rank)
        self.t_name=t_name
        self.t_dep=t_dep
        self.t_phone=t_phone
        print(self.t_dep,t_name,t_phone)
class Student(Teacher):
    def sval(self,s_name,roll,email):
        self.s_name=s_name
        self.roll=roll
        self.email=email
        print(self.s_name,self.roll,self.email)
st=Student('rahul',10,'rahul@gamil.com')
tt=Teacher("mary","computer",9895636365,'ekm',1)
st.print()
tt.print()