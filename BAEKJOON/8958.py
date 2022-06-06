n = int(input())

for i in range(n):
    s = list(str(input()))
    sum = 0
    count = 1
    for i in range(len(s)):
        if s[i] == 'O':
            sum += count
            count += 1
        else:
            count = 1

    print(sum)
