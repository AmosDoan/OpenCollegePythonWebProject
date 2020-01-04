result = input("시험 점수를 입력하세요 : ")

if int(result) >= 90:
    print("축하합니다! A등급 입니다.")
elif int(result) >= 80:
    print("축하합니다! B등급 입니다.")
else:
    print("불합격입니다.")