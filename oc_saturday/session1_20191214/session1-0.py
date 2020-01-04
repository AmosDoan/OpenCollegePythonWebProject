# a라는 라벨이 붙어있는 박스에 2라는 숫자를 저장한다.
a = 2
b = 3

# 위의 두 개의 변수(= 박스)들은 Integer Type이다.
print(type(a))
print(type(b))

# 정수형 변수는 사칙연산이 가능하다.
c = a + b
print(c)

c = a - b
print(c)

# 변수 type사이의 변경이 가능하다.
c = a * b
print(c)
print(type(c))

c = a / b
print(c)
print(type(c))

# Boolean type
d = True
e = False
print(type(d))
print(type(e))

# a랑 b랑 같냐??의 답은 Boolean False다
f = a == b
print(f)
print(a == b)

g = a < b
print(g)

h = a <= b
print(h)

i = a < b and a <= b
print(i)