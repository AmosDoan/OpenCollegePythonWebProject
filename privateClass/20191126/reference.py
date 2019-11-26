# 리스트의 생성
# 리스트 생성 방법은 두가지가 있다. 꺽쇠를 이용하는 방법 ([]), list 함수를 이용하여 빈 리스트를 만드는 방법
a = [2]

b = list()
b.append(2)

# list 함수에 다른 list를 input으로 넣어주면, 그 list를 복사한 새로운 list를 만든다.
c = list(b)

print(a)
print(b)
print(c)

# 리스트 연습
drink = ["soju", "beer", "wine"]
# Reference가 복사되는 친구들은 정수, 소수를 제외한 모든 친구들이다.
drink2 = drink
drink2[1] = "somac"
print(drink)

# 리스트 연습2
anju = ["감튀", "치킨"]
anju2 = list(anju)
anju2[1] = "노가리"
print(anju)

# 정수
a = 2
b = a
b = 3
print(a)

# 소수
a = 2.14
b = a
b = 3.14
print(a)

# String
name = "NimDohan"
# String의 replace 함수 안에서는 새로운 String을 만들어서 복사하고 그걸 변경 후 되돌려준다.
name2 = name.replace("N", "K")
print(name)

