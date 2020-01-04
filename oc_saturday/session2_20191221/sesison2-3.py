sum = 0
n = 0

while n < 11:
    sum = sum + n
    n = n + 1

print(sum)

a = 0
while a < 7:
    a = a + 1
    if a == 3:
        break
print(a)

gadgets = ['맥북', '아이맥', '갤럭시', '아이패드']
for gadget in gadgets:
    if gadget == '갤럭시':
        continue
    print(gadget + '은 애플 제품입니다.')