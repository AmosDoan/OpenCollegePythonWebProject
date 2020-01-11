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

result = calulator("add", 2, 3)
result = calulator("sub", 2, 3)
result = calulator("mul", 2, 3)
result = calulator("div", 2, 3)
