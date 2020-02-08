def deleteAddressBook():
    name = input("삭제할 사람의 이름을 입력하세요 : ")

    if name in addressBook.keys():
        del addressBook[name]
    else:
        print("해당 이름을 가진 전화번호가 없습니다.")

def addAddressBook():
    data = input("이름, 번호를 입력하세요 : ").split()
    addressBook[data[0]] = data[1]
    print("추가되었습니다.")


def queryAddressBook():
    if len(addressBook) == 0:
        print("등록된 번호가 없습니다.")
    else:
        for entry in addressBook.items():
            print('이름 :', entry[0], '번호 :', entry[1])


addressBook = dict()
while True:
    command = input('전화번호부를 조회하려면 조회 / 추가하려면 추가 / '
                '삭제하려면 삭제를 입력하세요 끝내려면 끝을 입력하세요')
    if command == "조회":
        queryAddressBook()
    elif command == "추가":
        addAddressBook()
    elif command == "삭제":
        deleteAddressBook()
    elif command == "끝":
        break

    else:
        print("명령어가 잘못되었습니다.")