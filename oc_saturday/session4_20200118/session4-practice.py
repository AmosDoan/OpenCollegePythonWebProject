class Car:
    def __init__(self, company, model, color):
        self.company = company
        self.model = model
        self.color = color
        self.oil = 1000

    def forward(self):
        self.oil -= 50
        print(self.company, self.model, self.color, "차량이 전진합니다. 남은 기름양:",
              self.oil)

    def reverse(self):
        # self.oil = self.oil - 30
        self.oil -= 30
        print(self.company, self.model, self.color, "차량이 전진합니다. 남은 기름양:",
              self.oil)

class ElectricCar(Car):

    def __init__(self, company, model, color):
        super().__init__(company, model, color)
        self.battery = 100

    def forward(self):
        self.battery -= 10
        print(self.company, self.model, self.color, "차량이 전진합니다. 남은 충전잔량:",
              self.battery)

    def reverse(self):
        self.battery -= 5
        print(self.company, self.model, self.color, "차량이 후진합니다. 남은 충전잔량:",
              self.battery)


hyundai = Car("hyundai", "sonata", "silver")
kia = Car("kia", "stinger", "red")
bmw = Car("bmw", "520d", "black")

print(hyundai.company)
hyundai.forward()
hyundai.reverse()
kia.forward()
kia.reverse()
bmw.forward()
bmw.reverse()

tesla = ElectricCar("telsa", "model x", "black")
tesla.forward()
tesla.reverse()
