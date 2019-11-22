menu = {'라면' : 4000, '만두' : 3500, '보쌈' : 28000}


while True:
    candidate = input("메뉴를 입력하세요 : ")

    if candidate in menu:
        gagyuk = menu[candidate]
        print(candidate + "는 " + str(gagyuk) + "원입니다.")
    else:
        print(candidate + "란 메뉴는 없습니다.")
