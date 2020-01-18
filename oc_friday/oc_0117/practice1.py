class Car:

    def __init__(self, company, model, color):
        self.company = company
        self.model = model
        self.color = color
        self.oil = 1000

    def forward(self):
        self.oil -= 50
        print(self.company, self.model, self.color,
              "차량 전진중입니다. 현재 기름양은 ",
              self.oil, "입니다.")

    def reverse(self):
        self.oil -= 30
        print(self.company, self.model, self.color,
              "차량 후진중입니다. 현재 기름양은 ",
              self.oil, "입니다.")

class ElctricCar(Car):

    def __init__(self, company, model, color):
        super().__init__(company, model, color)
        self.battery = 100

    def forward(self):
        self.battery -= 10
        print(self.company, self.model, self.color,
              "차량 전진중입니다. 현재 충전잔량은 ",
              self.battery, "입니다.")

    def reverse(self):
        self.battery -= 5
        print(self.company, self.model, self.color,
              "차량 후진중입니다. 현재 충전잔량은 ",
              self.battery, "입니다.")



hyundai = Car("hyundai", "avante", "blue")
hyundai.forward()
hyundai.reverse()

tesla = ElctricCar("telsa", "model x", "black")
tesla.forward()
tesla.reverse()
