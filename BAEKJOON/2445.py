n = int(input())

for i in range(n, 0, -1):
    print("*" * (n-i+1) + " " * (2*i-2) + "*" * (n-i+1))

for j in range(1, n+1):
    print("*" * (n-j) + " " * (2*j) + "*" * (n-j))
