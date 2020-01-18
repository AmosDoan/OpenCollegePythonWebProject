# Human Class (즉, 사람 객체를 만드는 틀!)
class Human:

    # Constructor (생성자) 실제 Object를
    # 만드는 함수!
    def __init__(self, name, gender, age, blood):
        self.name = name
        self.gender = gender
        self.age = age
        self.blood = blood

    def ageDouble(self):
        self.age = self.age * 2

    def introduceMyself(self):
        print('제 이름은', self.name, '입니다. 나이는', self.age, '이고',
              self.blood, '형 입니다.')

hakyung = Human("김하경", "female", 19, "B")
hakyung.introduceMyself()
hakyung.ageDouble()
hakyung.introduceMyself()

youngsub = Human("이용섭", "male", 20, "O")
youngsub.introduceMyself()
