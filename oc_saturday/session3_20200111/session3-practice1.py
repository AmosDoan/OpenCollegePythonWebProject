def calc(type, a, b):
    if type == "더하기":
        return a + b
    elif type == "빼기":
        return a - b
    elif type == "곱하기":
        return a * b
    elif type == "나누기":
        return a / b
    raise Exception("계산타입 오류")

while True:
    a = input("계산정보를 입력하세요: ")
    input_list = a.split()
    type = input_list[0]
    a = int(input_list[1])
    b = int(input_list[2])
    try:
        result = calc(type, a, b)
    except:
        print("계산 파라미터가 옳지 않습니다.")
        continue

    print("계산결과 : " + str(result))

