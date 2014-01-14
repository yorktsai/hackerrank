# https://www.hackerrank.com/challenges/chocolate-feast

nn = int(input())
for ni in range(0, nn):
    n, c, m = list(map(int, input().split()))
    chocolates = n // c
    wrappers = chocolates
    while wrappers >= m:
        c = wrappers // m
        chocolates += c
        wrappers = wrappers % m + c

    print(chocolates)

