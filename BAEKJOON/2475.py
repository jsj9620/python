a, b, c, d, e = list(map(int, input().split()))

result = (pow(a, 2) + pow(b, 2) + pow(c, 2) + pow(d, 2) + pow(e, 2)) % 10
print(result)
