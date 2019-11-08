menu = {'라면': '4000', '만두': '3500', '보쌈': '28000'}

menuName = input('메뉴를 입력하세요 : ')

isExistMenu = menuName in menu

if isExistMenu == True:
    cost = menu[menuName]
    print(menuName + "은 " + cost + "원 입니다. ")
elif isExistMenu == False:
    print(menuName + "이란 메뉴는 없습니다.")



