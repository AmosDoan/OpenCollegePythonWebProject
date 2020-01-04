# Human이라는 Class가 있고
class Human:

    # __init__ 함수는 Constructor 입니다.
    # Constructor를 이용하여 Object를 만들 수 있습니다.
    def __init__(self, name, age, gender, height, blood):
        self.name = name
        self.age = age
        self.gender = gender
        self.height = height
        self.blood = blood

    def sayName(self):
        print("제 이름은", self.name)

    def introduceMySelf(self):
        print("제 이름은", self.name, "이고 나이는", self.age, "입니다.")

dohanKim = Human("김도한", 20, "Male", 179, "AB")
yusunJung = Human("정유선", 31, "Female", 168, "O")

dohanKim.introduceMySelf()
yusunJung.introduceMySelf()