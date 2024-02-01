class Library:
    def __init__(self, name, location):
        self.name = name
        self.location = location
        self.books = []
        
    def add_book(self, book):
        for b in book:
            if type(b) != Book:
                raise ValueError('You can only add books to the library')
            else:
                self.books.append(b)
                
                
class Book:
    def __init__(self, title, author, genre):
        self.title = title
        self.author = author
        self.genre = genre
        self.library = None
        
    @property
    def library(self):
        return self._library
    
    @library.setter
    def library(self, new_library):
        if isinstance(new_library, Library) or new_library is None:
            self._library = new_library
            if new_library is not None:
                new_library.add_book(self)
        else:
            raise ValueError('Library must be a library')
        
if __name__ == "__main__":
    dpl = Library('Denver Public Library', 'Denver')
    LoC = Library('Library of Congress', 'Washington DC')
    Harry_Potter = Book('Harry Potter', 'JK Rowling', 'Fantasy')
    LoTR = Book('The Hobbit', 'JRR Tolkien', 'Fantasy')
    Catcher = Book('The Catcher in the Rye', 'JD Salinger', 'Fiction')
    Gatty = Book('The Great Gatsby', 'F Scott Fitzgerald', 'Fiction')
    Nicolas_Cage = Book('The Da Vinci Code', 'Dan Brown', 'Mystery')
    
    dpl.add_book([Harry_Potter, LoTR, Catcher, Gatty, Nicolas_Cage])
    print(dpl.books)