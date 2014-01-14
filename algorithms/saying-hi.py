# https://www.hackerrank.com/challenges/saying-hi

import re

n = int(input())
for x in range(0, n):
    line = input()

    if None != re.match("hi\\s[^d]+", line.lower()) or 'hi' == line.lower():
        print(line)
