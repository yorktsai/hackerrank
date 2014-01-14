# https://www.hackerrank.com/challenges/insertionsort1

def print_vec(vec):
    print(' '.join(map(str, vec)))

nn = int(input())
vec = list(map(int, input().split()))

for i in range(0, len(vec)):
    value = vec[i]
    j = i - 1
    while j >= 0 and vec[j] > value:
        vec[j + 1] = vec[j]
        print_vec(vec)
        j -= 1

    if j + 1 != i:
        vec[j + 1] = value
        print_vec(vec)
