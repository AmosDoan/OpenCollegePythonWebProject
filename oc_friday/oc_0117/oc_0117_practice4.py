#class Test:
#    test = 10
#
#print(Test.test)
#Test.test = 20
#print(Test.test)

class Test2:
    __test = 10

    def test(self):
        print(self.__test)

test = Test2()
#test.__test = 20
print(test.test())
