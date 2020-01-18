
class Car:

    def __init__(self, name):
        self.name = name

    def forward(self):
        return self.name + "전진합니다."

    def reverse(self):
        return self.name + "후진합니다."
