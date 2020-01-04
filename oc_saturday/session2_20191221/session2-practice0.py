menu = {'라면' : 4000, '만두' : 3500, '보쌈' : 28000}

menuName = input("메뉴를 입력하세요 : ")

if menuName in menu:
    cost = menu[menuName]
    print(menuName + "의 가격은 " + str(cost) + "원 입니다.")
else:
    print(menuName + "란 메뉴는 없습니다.")
