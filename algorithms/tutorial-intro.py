# https://www.hackerrank.com/challenges/tutorial-intro

v = int(input())
n = int(input())

vec = list(map(int, input().split()))

for i in range(0, n):
    if vec[i] == v:
        print(i)
