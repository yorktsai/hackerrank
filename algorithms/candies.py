# https://www.hackerrank.com/challenges/candies

import sys

n = int(input())
scores = []
candies = []

for x in range(0, n):
    score = int(input())
    scores.append(score)
    candies.append(1)

    i = len(scores) - 2
    if i >= 0:
        if scores[i] < score:
            candies[-1] = candies[i] + 1
        elif scores[i] > score:
            j = i
            while j >= 0 and scores[j] > scores[j+1] and candies[j] <= candies[j+1]:
                candies[j] += 1
                j -= 1

#for i in range(0, len(candies)):
#    print("{}: {}".format(scores[i], candies[i]))
print(sum(candies))

