# https://www.hackerrank.com/challenges/angry-children

n = int(input())
k = int(input())

vec = []
for i in range(0, n):
    vec.append(int(input()))

vec.sort()

m = vec[-1] - vec[len(vec) - k + 1]
for i in range(0, n-k+1):
    if vec[i+k-1] - vec[i] < m:
        m = vec[i+k-1] - vec[i]

print(m)
