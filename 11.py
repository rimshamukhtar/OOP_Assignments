# 11. Class Methods
# Assignment:
# Create a class Book with a class variable total_books. Add a class method increment_book_count() to increase the count when a new book is added.

class Book():
    total_books = 0

    @classmethod

    def increment_book_count (cls):
        cls.total_books += 1
        print(f"Total books now: {cls.total_books}")

Book.increment_book_count()
Book.increment_book_count() 

# kisi object ky through bi call kar sakty han
b1 = Book()
b1.increment_book_count()
