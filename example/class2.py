class Book2:
    __price = 15000

    def print(self):
        print(self.__price)

book2 = Book2()
book2.__price = 10000  # 값을 대입하지만 변하지 않는다.
book2.print()