result = 1

for _ in range(3):
    result = result * int(input())

temp = []
while result != 0:
    temp.append(result % 10)
    result = result // 10

for i in range(10):
    print(temp.count(i))
