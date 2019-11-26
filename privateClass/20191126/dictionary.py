phone = {"조세림" : "010-1234-5678", "김예슬" : "010-2345-3456", 3 : "tewt"}
print(phone["조세림"])
phone["김도한"] = "010-4567-6789"
print(phone)
print(type(phone))

phoneList = ["010-1234-5678", "010-2345-3456"]
nameList = ["조세림", "김예슬"]
print(nameList[0] + "번호는  : " + phoneList[0])

# Dictionary의 Key는 int, float, string, tuple이 가능하다.
tupleList = {("조세림", "학동") : "010-1234-5678"}
print(tupleList[("조세림", "학동")])
serim = tupleList.get(("조세림", "학동"))
print(serim)

# Dictionary 만드는 방법 2.
# dict 함수는 key가 string일지라도 따옴표를 붙이지 않는다.
dictionary = dict(조세림 = "010-1234-5677", 김에슬 = "010-2345-3456")
print(dictionary)

if "김도한" in dictionary:
    print("김도한이 있습니다!")
else:
    print("김도한이 없습니다!")
