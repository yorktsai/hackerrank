# https://www.hackerrank.com/challenges/stockmax

import sys

cases = int(input())

for case in range(0, cases):
    n = int(input())
    prices = list(map(int, input().split()))

    profit = 0
    current_max = prices[-1]
    for i in range(len(prices)-1, -1, -1):
        if prices[i] >= current_max:
            current_max = prices[i]

        profit += current_max - prices[i]

    print(profit)
