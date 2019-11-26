# 20191113 표준 출력 연습
print("Hello")
print("안녕")
print("1111")

# 변수 연습
a = 2
b = 3
c = "hello"
print(a)
print(b)
print(c)
print(4)

# 변수의 타입
# 정수형 변수 (Integer)
a = 2
# 실수형 변수 (Float)
b = 3.14
# String
c = "hello"

print(type(a))
print(type(b))
print(type(c))

# 표준 입력
#a = input("입력하세요 : ")
#print(a)
#
#a = input("첫번째 수를 입력하세요 : ")
#b = input("두번째 수를 입력하세요 : ")
#c = int(a) + int(b)
print(c)

# 이 의미는 사람이 2+3을 하고 싶으면 2 3을 입력한다는 뜻이다.
a = input("첫번째 수와 두 번째 수를 공백으로 구분해서 입력하세요 : ")
b = a.split(" ")
c = int(b[0]) + int(b[1])
print(c)

