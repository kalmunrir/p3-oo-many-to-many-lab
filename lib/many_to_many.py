class Author:

    all = []

    def __init__(self, name):
        self.name = name
        Author.all.append(self)

    @property
    def name(self):
        return self._name
    @name.setter
    def name(self, name):
        if isinstance(name, str):
            self._name = name
        else:
            raise Exception("Author's name should be a string")
        
    def contracts(self):
        return([ contract for contract in Contract.all if contract.author == self])
    def books(self):
        return([ contract.book for contract in self.contracts()])
    def sign_contract(self, book, date, royalties):
        new_contract = Contract(self, book, date, royalties)
        return new_contract
    def total_royalties(self):
        return (sum([contract.royalties for contract in self.contracts()]))

class Book:

    all = []

    def __init__(self, title):
        self.title = title
        Book.all.append(self)

    @property
    def title(self):
        return self._title
    @title.setter
    def title(self, title):
        if isinstance(title, str):
            self._title = title
        else:
            raise Exception("Book title should be a string")
        
    def contracts(self):
        return ([contract for contract in Contract.all if contract.book == self])
    def authors(self):
        return ([contract.author for contract in self.contracts()])


class Contract:

    all = []

    def __init__(self, author, book, date, royalties):
        self.author = author
        self.book = book
        self.date = date
        self.royalties = royalties
        Contract.all.append(self)

    @property
    def author(self):
        return self._author
    @author.setter
    def author(self, author):
        if isinstance(author, Author):
            self._author = author
        else:
            raise Exception("Author should be of type Author")
    @property
    def book(self):
        return self._book
    @book.setter
    def book(self, book):
        if isinstance(book, Book):
            self._book = book
        else:
            raise Exception("Book should be of type Book")
    @property
    def date(self):
        return self._date
    @date.setter
    def date(self, date):
        if isinstance(date, str):
            self._date = date
        else:
            raise Exception("Date should be a string")
    @property
    def royalties(self):
        return self._royalties
    @royalties.setter
    def royalties(self, royalties):
        if isinstance(royalties, int):
            self._royalties = royalties
        else:
            raise Exception("Royalties should be an integer")
        
    @classmethod
    def contracts_by_date(cls):
        return (sorted(cls.all, key = lambda contract: contract.date))