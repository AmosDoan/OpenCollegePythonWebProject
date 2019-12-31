
def 더하기(숫자1, 숫자2):
    결과 = 숫자1 + 숫자2
    return 결과

def sayHello():
    return "Hello"


def printHello():
    print("Hello")

결과1 = 더하기(2, 3)
print(결과1)
결과2 = 더하기(1, 4)
print(결과2)

# 재료가 없는 함수
result = sayHello()
print(result)

# 리턴값이 없는 함수
printHello()
