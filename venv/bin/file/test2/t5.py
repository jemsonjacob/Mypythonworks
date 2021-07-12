class Teacher:
    def tval(self,tname,tage,coleege):
        self.tname=tname
        self.tage=tage
        self.coleege=coleege
        print(self.tage,self.coleege,self.tname)
class Student(Teacher):
    def tval(self, tname, tage, coleege):
        self.tname = tname
        self.tage = tage
        self.coleege = coleege
        print(self.tage, self.coleege, self.tname)

s=Student()
s.tval(37,'uma','matha college')
s.tval(38,'ammu',"st.marys")