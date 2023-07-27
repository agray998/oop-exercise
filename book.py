'''
Create a class Book. Each book object should have the attributes: 
- title
- author (default unknown) 
- number of pages
- genre
- ISBN. 
The class should define the following methods:
- __init__ to set the attributes described above
- __str__ to print a description of the book
- a search method which returns all books by a given author (requires tracking of objects) - if there are no books by the given author return an empty list
- a method to check the validity of a given ISBN-13 - should return true if the ISBN is valid, false otherwise
As an additional stretch goal, create 2 subclasses for specific 
genres and override the __init__ method and __str__ methods appropriately
'''

class Book():
    '''
    Represents book objects. Each book has a title, author, genre, number of pages and isbn.
    The class has a static attribute books[] which tracks book objects. The class also has functionality
    to write book object reprs to a file, and to load books from said file into the books[] list 
    on startup.
    '''
    books = []

    @staticmethod
    def initialise_list(bookfile: str) -> None:
        '''
        Loads book objects found in the specified file into the books[] list.
        bookfile must exist prior to calling this method.
        '''
        with open(bookfile, 'r') as file:
            for book in file:
                eval(book)

    def __init__(self, title: str, pages: int, isbn: str, genre: str, fromrepr: bool = False, author: str = "Unknown", bookfile: str = "books.list") -> None:
        '''
        Initialise book objects with title, author, number of pages, genre and ISBN. Also adds book to books[] list and, if not being recreated 
        from a repr, writes the book's repr to bookfile
        '''
        self.title = title
        self.pages = pages
        self.isbn = isbn
        self.genre = genre
        self.author = author
        Book.books.append(self)
        if not fromrepr:
            with open(bookfile, 'a') as file:
                file.write(self.__repr__() + '\n')
    
    @staticmethod
    def valid_isbn(isbn: str) -> bool:
        '''
        Determines whether the ISBN provided is valid or not based on the check-digit logic
        Only supports ISBN-13 format. Dashes in the ISBN are optional.
        '''
        digits = ''.join(isbn.split('-'))
        if len(digits) != 13:
            return False
        diglist = [int(digit) for digit in digits]
        return ((sum([diglist[i] for i in range(12) if i % 2 == 0]) + 3 * sum([diglist[i] for i in range(12) if i % 2 != 0]) + diglist[-1]) % 10) == 0
    
    @staticmethod
    def search(author: str) -> list:
        '''
        Returns a list of all books in the books[] list which are by the given author
        If no books have the given author an empty list is returned
        '''
        return list(filter(lambda book: book.author == author, Book.books))

    def __str__(self) -> str:
        return f"Written by {self.author}, {self.title} is a gripping {self.pages}-page {self.genre} novel"
    
    def __repr__(self) -> str:
        return f"Book('{self.title}', {self.pages}, '{self.isbn}', '{self.genre}', fromrepr=True, author='{self.author}')"


class SciFiNovel(Book):
    '''
    Subclass of Book. Exposes same functionality. 
    Overrides __init__ and __str__ to be sci-fi specific.
    '''
    def __init__(self, title, pages, isbn, fromrepr = False, author = "Unknown", bookfile="books.list"):
        super().__init__(title=title, pages=pages, isbn=isbn, genre="sci-fi", fromrepr=fromrepr, author=author, bookfile=bookfile)
    
    def __str__(self):
        return f"Written by {self.author}, {self.title} is a thrilling {self.pages}-page science fiction masterpiece"
    
class FantasyNovel(Book):
    '''
    Subclass of Book. Exposes same functionality. 
    Overrides __init__ and __str__ to be fantasy-specific.
    '''
    def __init__(self, title, pages, isbn, fromrepr = False, author = "Unknown", bookfile="books.list"):
        super().__init__(title=title, pages=pages, isbn=isbn, genre="fantasy", fromrepr=fromrepr, author=author, bookfile=bookfile)
    
    def __str__(self):
        return f"Written by {self.author}, {self.title} is an enchanting {self.pages}-page masterclass in fantasy worldbuilding"