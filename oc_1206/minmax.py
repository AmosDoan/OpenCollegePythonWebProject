numbers = [1, 100, -1, 30, 5, 99, 45, 30, -2, -10]

min = numbers[0]

for number in numbers:
    if number < min:
        min = number

print("최소값은 " + str(min))

