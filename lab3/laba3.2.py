from LibsBooks import Libs
from Books import Books


lib = Libs(1, '51 Some str., NY')
lib += Books('Leo Tolstoi', 'War and Peace')
lib += Books('Charles Dickens', 'David Copperfield')
for book in lib:
    print(book)
    print(book.tag())