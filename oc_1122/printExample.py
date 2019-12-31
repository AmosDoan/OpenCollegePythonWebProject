command = input()
numbers = command.split()


result = int(numbers[0]) - int(numbers[1])

if result < 0:
    print('<')
elif result > 0:
    print('>')
else:
    print('==')
