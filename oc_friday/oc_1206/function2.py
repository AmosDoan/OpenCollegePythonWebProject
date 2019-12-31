# default parameter를 지정할 수 있다.
def add(a, b = 2):
    return a + b

def multiplyQuadraple(a, b = 1, c = 2, d = 3):
    return a * b * c

result = add(1, 3)
print(result)

result = add(3)
print(result)

