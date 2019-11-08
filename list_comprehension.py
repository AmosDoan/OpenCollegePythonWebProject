openCollegeMembers = ['이광우', '류은진', '김유준', '한승욱',
                      '신봉건', '정유선', '염재희']

nimMembers = []
for i in openCollegeMembers:
    nimMembers.append(i + "님")

print(nimMembers)


nimMembers2 = [member + "님" for member in openCollegeMembers]
print(nimMembers2)
