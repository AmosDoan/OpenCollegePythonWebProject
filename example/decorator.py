class Car:

    @property
    def color(self):
        print('get Color', self.__color, 'gogo')
        return self.__color

    @color.setter
    def color(self, color):
        print('set Color', color, 'gogo')
        self.__color = color

    @color.deleter
    def color(self):
        self.__color = 'black'

car = Car()
car.color = 3000
print(car.color)
del(car.color)

