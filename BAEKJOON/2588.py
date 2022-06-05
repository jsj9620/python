a = int(input())
b = int(input())
tempVar = b
temp = []
while b != 0:
    temp.append(b % 10)
    b = b // 10

for i in range(3):
    print(a * temp[i])

print(a*tempVar)
