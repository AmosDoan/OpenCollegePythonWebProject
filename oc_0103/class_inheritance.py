class Book:

    def __init__(self, title, price):
        self.title = title
        self.price = price

    def printPrice(self, num):
        print(num, "권의 책", self.title, "의 가격은",
              self.price * num, "원 입니다.")


class ColorBook(Book):

    def __init__(self, title, price, color):
        super().__init__(title, price)
        self.color = color

    def printColor(self):
        print(self.color, "Coloring 중입니다.")

    def printPrice(self, num):
        super().printPrice(num)
        print("부자시네여")


book1 = Book("훔쳐보는 여자", 15000)
book1.printPrice(2)

book2 = ColorBook("빨간 그림책", 30000, "pink")
book2.printPrice(3)
book2.printColor()
