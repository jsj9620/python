temp = []
temp2 = []
for _ in range(10):
    temp.append(int(input()))

for i in range(10):
    temp2.append(temp[i] % 42)

temp2 = set(temp2)
print(len(temp2))
