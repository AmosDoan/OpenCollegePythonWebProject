class Book:
    description = "이 클래스는 book을 만들기 위한 class"

    def __init__(self, name, price):
        self.name = name
        self.price = price

    def printInfo(self):
        print("책 이름", self.name, "가격", self.price)

    @classmethod
    def test(cls):
        print("test")

print(Book.description)
Book.test()

book = Book("해리포터", 5000)
book.printInfo()
