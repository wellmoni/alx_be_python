class Book:
    def __init__(self, title, author):

        self.title = title
        self.author = author

    def __str__(self):
        return f"'{self.title}' by {self.author}"
class EBook(Book):
    def __init__(self, title,author, file_size):
        
        super().__init__(title, author)
        self.file_size = file_size
    def __str__(self):
        return f"{super().__str__()} [EBook - {self.file_size}MB]"

class PrintBook(Book):

        def __init__(self, title, author, page_count):
            super().__init_(title, author)
            self.page_count = page_count
        def __str__(self):
            return f"{super().__str__()} [PrintBook - {self.page_count} pages]"
class Library:

        def __init__(self):
            self.books = []
        def add_book(self, book):

            if isinstance(book, Book):
                self.books.append(book)
            else:
                raise TypeError ("Oly instances of Book, EBook, or PrintBook can be added.")

            def list_books(self):
                if not self.books:

                    print ("THe Library is empty.")
                else:
                    print ("Library COllection:")

                    for book in self.books:
                        print (f" -{book}")

