def multiplyAndDivide(a, b):
    return a * b, a / b


def calc(a, b):
    return a + b, a - b, a * b, a / b


print(type(multiplyAndDivide(1, 2)))

result = calc(2, 3)
print(result)

multiplyResult, divideResult = multiplyAndDivide(2, 3)
print(multiplyResult)
print(divideResult)
