# 리스트는 각각의 Element에 의미를 부여하기 어렵다.
a = list()
a.append("010-1234-5678")
a.append("010-2345-6789")

firstValueInA = a[0]

# 대안으로 나온 Dicitonary
b = {"김도한": ["010-7178-0444", "010-7168-0444"], "이용섭": "010-1234-5677"}
dohanValueInB = b["김도한"]
print(type(dohanValueInB))

phoneDictionary = {"김도한" : ["010-7178-0473", "성남시 수정구 복정동"]}

c = dict(김도한 = "복정", 이용섭 = "대전")
print(c)

is_heywon_exist = "조혜원" in c
is_dohan_exist = "김도한" in c
print(is_heywon_exist)
print(is_dohan_exist)

if is_heywon_exist:
    print(c["조혜원"])
else:
    print("혜원님은 Dictionary에 없습니다.")

c["조혜원"] = "010-7890-1234"
c.pop("김도한")

is_dohan_exist = "김도한" in c
is_heywon_exist = "조혜원" in c

print(is_heywon_exist)
print("조혜원" in c)

print(is_dohan_exist)
print("김도한" in c)
