class Author:
    def __init__(self, name):
        self.name = name
        self._contracts = []

    def contracts(self):
        return self._contracts

    def books(self):
        return list({contract.book for contract in self._contracts})

    def sign_contract(self, book, date, royalties):
        return Contract(self, book, date, royalties)

    def total_royalties(self):
        return sum(contract.royalties for contract in self._contracts)


class Book:
    def __init__(self, title):
        self.title = title
        self._contracts = []

    def contracts(self):
        return self._contracts

    def authors(self):
        return list({contract.author for contract in self._contracts})


class Contract:
    all = []

    def __init__(self, author, book, date, royalties):
        if not isinstance(author, Author):
            raise Exception()
        if not isinstance(book, Book):
            raise Exception()
        if not isinstance(date, str):
            raise Exception()
        if not isinstance(royalties, int):
            raise Exception()

        self.author = author
        self.book = book
        self.date = date
        self.royalties = royalties

        author._contracts.append(self)
        book._contracts.append(self)
        Contract.all.append(self)

    @classmethod
    def contracts_by_date(cls, date):
        return [contract for contract in cls.all if contract.date == date]
