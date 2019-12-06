def calc(calcType, a, b):
    if calcType == "더하기":
        return a + b
    if calcType == "빼기":
        return a - b
    if calcType == "곱하기":
        return a * b
    if calcType == "나누기":
        return a / b


a = input("계산정보를 입력하세요: ")
받은것들 = a.split()
print(type(받은것들))
calcType = 받은것들[0]
a = int(받은것들[1])
b = int(받은것들[2])
result = calc(calcType, a, b)

if result == None:
    print("그런 계산방법은 없습니다.")
else:
    print("계산결과 : " + str(result))