names = ["신봉건", "고유빈", "김진옥", "이광우"]
nimNames = []

for name in names:
    nimNames.append(name + "님")

for nimName in nimNames:
    print(nimName)

print("========================")
nimNames2 = [name + "님" for name in names]

for nimName in nimNames2:
    print(nimName)


