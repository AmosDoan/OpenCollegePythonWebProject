class Car:

    def __init__(self, manufacturer, model, color):
        self.manufacturer = manufacturer
        self.model = model
        self.color = color
        self.fuel = 1000

    def forward(self):
        self.fuel = self.fuel - 50
        print(self.manufacturer, self.model, self.color,
              "차량이 전진 중입니다! 현재 기름양은",
              self.fuel, "입니다.")

    def reverse(self):
        self.fuel = self.fuel - 30
        print(self.manufacturer, self.model, self.color,
              "차량이 후진 중입니다! 현재 기름양은",
              self.fuel, "입니다.")

class ElectricCar(Car):

    def __init__(self, manufacturer, model, color):
        super().__init__(manufacturer, model, color)
        self.battery = 100

    def forward(self):
        self.battery = self.battery - 10
        print(self.manufacturer, self.model, self.color,
              "차량이 전진 중입니다! 현재 충전량은",
              self.battery, "% 입니다.")

    def reverse(self):
        self.battery = self.battery - 5
        print(self.manufacturer, self.model, self.color,
              "차량이 후진 중입니다! 현재 충전량은",
              self.battery, "% 입니다.")


car1 = Car("BMW", "420i", "White")
car2 = Car("Hyundai", "avante", "black")
car3 = Car("Kia", "stinger", "Red")

car1.forward()
car1.reverse()
car2.forward()
car2.reverse()
car3.forward()
car3.reverse()

electricCar1 = ElectricCar("TESLA", "Model X", "Black")
electricCar2 = ElectricCar("TESLA", "Model 3", "Black")
electricCar3 = ElectricCar("TESLA", "Model X", "White")

electricCar1.forward()
electricCar1.reverse()
electricCar2.forward()
electricCar2.reverse()
electricCar3.forward()
electricCar3.reverse()
