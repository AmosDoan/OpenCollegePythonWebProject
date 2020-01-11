def calulator(calcType, a, b):

    if calcType == "add":
        return a + b
    elif calcType == "sub":
        return a - b
    elif calcType == "mul":
        return a * b
    elif calcType == "div":
        return a / b
    else:
        return "올바른 계산 타입이 아닙니다."


def sayGoodBye():
    return "Good bye!"


def printGoodBye():
    print(sayGoodBye())

try:
    result1 = calulator("add", 2, 3)
    print(result1)

    result1 = calulator(a=2, b=3, calcType="add")
    print(result1)

    print(calulator("add", 2, 3))

    result2 = calulator("sub", 2, 3)
    print(result2)
    result3 = calulator("mul", 2, 3)
    print(result3)
    result4 = calulator("div", 2, 3)
    print(result4)
    result5 = calulator("div", 2, 0)
    print(result5)
except:
    print("Error 발생했습니다.")


print(sayGoodBye())
printGoodBye()
