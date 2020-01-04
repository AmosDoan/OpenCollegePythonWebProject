friends = ['신봉건', '염재희', '류은진', '이광우', '정유선']
for friend in friends:
    print("친구 " + friend)

numbers = list(range(10))
print(numbers)

for i in numbers:
    print(i * "*")

a = {'김도한' : '010-7188-7777', '신봉건' : '010-9798-8888'}

for name in a.keys():
    print(name)

for phone_number in a.values():
    print(phone_number)
