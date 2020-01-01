class TestClass:
    num = 0

    def __init__(self):
        TestClass.num = TestClass.num + 1

    @classmethod
    def numberOfInstance(cls):
        print("현재 갯수 :", cls.num)

test1 = TestClass()
TestClass.numberOfInstance()

test2 = TestClass()
TestClass.numberOfInstance()
