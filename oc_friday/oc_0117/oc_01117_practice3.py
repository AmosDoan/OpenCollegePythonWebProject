class Book:
    def __init__(self, title, price):
        self.title = title
        self.price = price

    def printPrice(self):
        print("책 이름은", self.title,
              "책 가격은", self.price)

class ColoringBook(Book):

    def __init__(self, title, price, color):
        super().__init__(price, title)
        self.color = color

    def printPrice(self):
        print("책 이름은", self.title,
              "책 가격은", self.price,
              "책 컬러는", self.color)



book = Book("해리포터", 10000)
book.printPrice()

colorBook = ColoringBook("색칠하기", 5, "White")
colorBook.printPrice()
print(colorBook.color)

