# https://www.hackerrank.com/challenges/correctness-invariant

nn = int(input())
vec = list(map(int, input().split()))
vec.sort()
print(' '.join(map(str, vec)))
