class Book:
    def bval(self,Library_name, book_name, author, pages):
        self.Library_name=Library_name
        self.book_name=book_name
        self.author=author
        self.pages=pages
    def pval(self):
        print(self.Library_name)
        print(self.book_name)
        print(self.author)
        print(self.pages)
b=Book()
b.bval('public library','chemeen','Thakazhi',550)
b.pval()

