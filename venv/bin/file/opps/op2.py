class Book:
    def bookval(self, book_name, author, pages, library):
        self.book_name = book_name
        self.author = author
        self.pages = pages
        self.library = library

    def difbook(self):
        print(self.book_name)
        print(self.author)
        print(self.pages)
        print(self.library)


obj = Book()
obj.bookval("harry potter", "J.K rowling", 1000, "public bok")
obj.difbook()
