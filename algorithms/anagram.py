# https://www.hackerrank.com/challenges/anagram

n = int(input())
for i in range(0, n):
    str = input()
    if len(str) % 2 > 0:
        print(-1)
        continue

    str1 = str[:len(str) // 2]
    str2 = str[len(str) // 2:]

    d = {}
    for c in str1:
        if not c in d:
            d[c] = 0

        d[c] += 1

    count = 0
    for c in str2:
        if c in d and d[c] > 0:
            d[c] -= 1
        else:
            count += 1

    print(count)

