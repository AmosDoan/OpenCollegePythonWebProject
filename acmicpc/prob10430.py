l = input().split()

a = int(l[0])
b = int(l[1])
c = int(l[2])

print((a + b) % c)
print((a % c + b % c) % c)
print((a * b) % c)
print((a % c * b % c) % c)
