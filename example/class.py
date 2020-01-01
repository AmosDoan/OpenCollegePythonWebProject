class Human:
    name = '김도한'
    age = 32
    address = '복정동'
    blood = 'A'
    __private = 'test'

    def test(self):
        print(self.__private)

human = Human()
human.__private = 'test2'
human.test()
