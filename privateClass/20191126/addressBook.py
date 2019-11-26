addressBook = {}
while True:
    command = input("추가하려면 추가, 삭제하려면 삭제, 확인하려면 확인을, 끝내고 싶으면 끝을 입력하세요 : ")

    if command == "추가":
        info = input("이름, 번호를 입력하시오 : ")
        infoList = info.split()

        addressBook[infoList[0]] = infoList[1]

        print("추가 되었습니다. : " + addressBook[infoList[0]])
    elif command == "삭제":
        info = input("삭제할 사람의 이름을 입력하세요 : ")
        addressBook.pop(info)
    elif command == "확인":
        print(addressBook)
    elif command == "끝":
        break


