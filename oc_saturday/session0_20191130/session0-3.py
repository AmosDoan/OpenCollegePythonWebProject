# 여기서는 스트링 변수를 알아볼 것이다.
name = "김도한"
print(name)

# print 함수에 바로 문자열을 사용할 수 있다.
print('안녕')
print("하세요")

# 문자열은 작은 따옴표로도 푯현할 수 있다.
대사 = '그가 말했다. "안녕"'
print(대사)

# 문자열 더하기
a = name + 대사
print(a)

# 문자열 곱하기
print(a * 2)

# 문자열 나누기
ㅁ = '2 3'
나눈결과 = ㅁ.split()
print(나눈결과[0])
print(type(나눈결과[0]))
print(나눈결과[1])

# 문자열 나누기 2
a = "1_2_3_4_5"
result = a.split('_')
print(result[0])
print(result[1])
print(result[2])
