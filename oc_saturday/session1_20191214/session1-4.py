openCollegeSaturdayPython = list()
openCollegeSaturdayPython.append("은지님")
openCollegeSaturdayPython.append("혜원님")
openCollegeSaturdayPython.append("근호님")
openCollegeSaturdayPython.append("선혜님")
openCollegeSaturdayPython.append("용섭님")
openCollegeSaturdayPython.append("하경님")

print(openCollegeSaturdayPython)

openCollegeSaturdayPython.remove("선혜님")
print(openCollegeSaturdayPython)


a = [-1, 2, 100, 0, 3]
a.sort()
print(a)

a.sort(reverse=True)
print(a)

b = [1, 2, 100, -100, -200]
c = sorted(b)
print(b)
print(c)

# 변경 불가능한 리스트는 튜플이다!
a = ("은지님", "용섭님", "하경님", "근호님", "혜원")

