class Human:

    def __init__(self, name, age, blood):
        self.name = name
        self.age = age
        self.blood = blood

    def introduceMyself(self):
        print("제 이름은", self.name, "이고",
              self.age, "살입니다.")

dohan = Human("김도한", 20, "A")
dohan.introduceMyself()

