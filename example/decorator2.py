class Book:
    def __init__(self, t, p):
        self.title = t
        self.__price = p

    @property
    def price(self):
        return self.__price

    @price.setter
    def price(self, p):
        self.__price = p

    @price.deleter
    def price(self):
        self.__price = 0

book1 = Book('그림책', 10000)
book1.price
print(book1.price)
del(book1.price)