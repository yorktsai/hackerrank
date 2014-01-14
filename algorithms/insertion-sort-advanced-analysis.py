# https://www.hackerrank.com/challenges/insertion-sort

def merge(v, start, end):
    if end - start <= 1:
        return 0

    if end - start == 2:
        if v[start] > v[start + 1]:
            tmp = v[start]
            v[start] = v[start + 1]
            v[start + 1] = tmp
            return 1

        return 0

    # print(str(start) + ', ' + str(end))

    mid = start + (end - start) // 2
    count = merge(v, start, mid) + merge(v, mid, end)

    v1 = v[start:mid]
    index = start
    i, j = 0, mid
    while i < len(v1) and j < end:
        if v1[i] <= v[j]:
            v[index] = v1[i]
            i += 1
        elif v1[i] > v[j]:
            v[index] = v[j]
            count += mid - start - i
            j += 1

        index += 1

    while i < len(v1):
        v[index] = v1[i]
        index += 1
        i += 1

    while j < end:
        v[index] = v[j]
        index += 1
        j += 1

    #print('count = ' + str(count))
    return count

nn = int(input())
for ni in range(0, nn):
    n = int(input())
    vec = list(map(int, input().split()))
    print(merge(vec, 0, len(vec)))

