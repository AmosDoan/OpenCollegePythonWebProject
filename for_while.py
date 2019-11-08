friends = ['김도한', '이광우', '한승욱', '류은진', '김유준',
           '정유선', '고유빈', '염재희', '김진옥']

print('오늘 나오신분은 ' + friends[0] + '입니다.')
print('오늘 나오신분은 ' + friends[1] + '입니다.')
print('오늘 나오신분은 ' + friends[2] + '입니다.')
print('오늘 나오신분은 ' + friends[3] + '입니다.')
print('오늘 나오신분은 ' + friends[4] + '입니다.')
print('오늘 나오신분은 ' + friends[5] + '입니다.')
print('오늘 나오신분은 ' + friends[6] + '입니다.')
print('오늘 나오신분은 ' + friends[7] + '입니다.')

print('====== 아래는 for문 =====')
for name in friends:
    print('오늘 나오신분은 ' + name + '입니다.')

출석부 = {'이광우': '출석', '한승욱': '출석',
       '류은진': '출석', '김도한': '출석',
       '정유선': '결석', '김유준': '조퇴',
       '염재희': '결혼', '박지영': '격무에시달림',
       '고유빈': '대학생인데..', '염보현': '송별화'}

print(출석부.items())

for element in 출석부.items():
    if element[1] == '출석':
        print(element[0] + '님은 VIP이십니다.')
    else:
        print(element[0] + '님은 아쉬우신분들입니다. 사유 : ' +
              element[1])


