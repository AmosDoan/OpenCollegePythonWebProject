def calcMax(number_list_str):
    number_list = [int(i) for i in number_list_str]
    max = number_list[0]
    for number in number_list:
        if number > max:
            max = number

    return max


def calcMin(number_list_str):
    number_list = []
    for number_str in number_list_str:
        number_list.append(int(number_str))

    min = number_list[0]
    for number in number_list:
        if number < min:
            min = number

    return min

def calcAvg(number_list_str):
    number_list = list(map(int, number_list_str))

    sum = 0

    for number in number_list:
        sum = sum + number

    return sum / len(number_list)


numbers = input("숫자들을 입력하세요: ")
max_result = calcMax(numbers.split())
min_result = calcMin(numbers.split())
avg_result = calcAvg(numbers.split())

print("최댓값 : " + str(max_result))
print("최솟값 : " + str(min_result))
print("평균값 : " + str(avg_result))