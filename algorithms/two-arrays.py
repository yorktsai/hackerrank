# https://www.hackerrank.com/challenges/two-arrays

nn = int(input())

for i in range(0, nn):
    n, k = list(map(int, input().split()))
    vec_a = list(map(int, input().split()))
    vec_b = list(map(int, input().split()))
    vec_a.sort()
    vec_b.sort(reverse=True)
    i = 0
    j = 0
    answer = True
    while i < n and j < n:
        if vec_a[i] + vec_b[j] < k:
            answer = False
            break

        i += 1
        j += 1

    if answer:
        print("YES")
    else:
        print("NO")
