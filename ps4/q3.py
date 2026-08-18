"""ITERATOR PATTERN
A university develops a Library Management System that stores thousands of
books across categories:
• Computer Science
• Electronics
• Mechanical
• Literature
• Journals & Magazines

Different users need to traverse books in different ways:
• Student → Browse all books
• Librarian → Check issued books
• Admin → Generate inventory report
• Visitor → Browse available books only

The system must allow traversal without exposing internal storage structure.
"""

from abc import ABC, abstractmethod

class Book:
    def __init__(self, title, category, is_issued=False):
        self.title = title
        self.category = category
        self.is_issued = is_issued

    def __str__(self):
        return f"{self.title} ({self.category}) - {'Issued' if self.is_issued else 'Available'}"
    
    def __repr__(self):
        return self.__str__()
    
    
class Library:
    def __init__(self):
        self.books = []

    def add_book(self, book):
        self.books.append(book)

    def create_iterator(self, user_type):
        iterator_class = {
            "student": StudentIterator,
            "librarian": LibrarianIterator,
            "admin": AdminIterator,
            "visitor": VisitorIterator,
        }.get(user_type.lower())
        if iterator_class is None:
            raise ValueError(f"Unknown user type: {user_type}")
        return iterator_class(self.books)

    
class BookIterator(ABC):
    @abstractmethod
    def has_next(self):
        pass

    @abstractmethod
    def next(self):
        pass

    
class StudentIterator(BookIterator):
    def __init__(self, books):
        self.books = books
        self.index = 0

    def has_next(self):
        return self.index < len(self.books)

    def next(self):
        if self.has_next():
            book = self.books[self.index]
            self.index += 1
            return book
        else:
            raise StopIteration
        
        
class LibrarianIterator(BookIterator):
    def __init__(self, books):
        self.books = [book for book in books if book.is_issued]
        self.index = 0

    def has_next(self):
        return self.index < len(self.books)

    def next(self):
        if self.has_next():
            book = self.books[self.index]
            self.index += 1
            return book
        else:
            raise StopIteration
        
        
class AdminIterator(BookIterator):
    def __init__(self, books):
        self.books = books
        self.index = 0

    def has_next(self):
        return self.index < len(self.books)

    def next(self):
        if self.has_next():
            book = self.books[self.index]
            self.index += 1
            return book
        else:
            raise StopIteration
        
        
class VisitorIterator(BookIterator):
    def __init__(self, books):
        self.books = [book for book in books if not book.is_issued]
        self.index = 0

    def has_next(self):
        return self.index < len(self.books)

    def next(self):
        if self.has_next():
            book = self.books[self.index]
            self.index += 1
            return book
        else:
            raise StopIteration


class LibraryUser(ABC):
    @abstractmethod
    def traverse_books(self, library):
        pass
    
class Student(LibraryUser):
    def traverse_books(self, library):
        print("Student browsing all books:")
        iterator = library.create_iterator("student")
        while iterator.has_next():
            print(iterator.next())
            
class Librarian(LibraryUser):
    def traverse_books(self, library):
        print("Librarian checking issued books:")
        iterator = library.create_iterator("librarian")
        while iterator.has_next():
            print(iterator.next())
                
class Admin(LibraryUser):
    def traverse_books(self, library):
        print("Admin generating inventory report:")
        iterator = library.create_iterator("admin")
        while iterator.has_next():
            print(iterator.next())
            
            
class Visitor(LibraryUser):
    def traverse_books(self, library):
        print("Visitor browsing available books:")
        iterator = library.create_iterator("visitor")
        while iterator.has_next():
            print(iterator.next())
        
class LibraryManagementSystem:
    def __init__(self):
        self.library = Library()

    def add_book(self, title, category, is_issued=False):
        book = Book(title, category, is_issued)
        self.library.add_book(book)
            

def main():
    lms = LibraryManagementSystem()
    lms.add_book("Introduction to Algorithms", "Computer Science")
    lms.add_book("Digital Design", "Electronics", is_issued=True)
    lms.add_book("Thermodynamics", "Mechanical")
    lms.add_book("Pride and Prejudice", "Literature")
    lms.add_book("National Geographic", "Journals & Magazines", is_issued=True)

    student = Student()
    librarian = Librarian()
    admin = Admin()
    visitor = Visitor()

    student.traverse_books(lms.library)
    librarian.traverse_books(lms.library)
    admin.traverse_books(lms.library)
    visitor.traverse_books(lms.library)

if __name__ == "__main__":
    main()