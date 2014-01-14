# https://www.hackerrank.com/challenges/red-john-is-back

import math
import bisect

def memorize(dp, n):
    if n <= 0:
        return 0

    if n > 0 and n <= 3:
        return 1

    if n == 4:
        return 2

    if n in dp:
        return dp[n]

    p = memorize(dp, n-4) + memorize(dp, n-1)
    dp[n] = p

    return dp[n]

def build_prime(primes, n):
    for i in range(primes[-1] + 1, int(math.ceil(math.sqrt(n))) + 1):
        is_prime = True
        for j in primes:
            if i % j == 0:
                is_prime = False
                break
        
        if is_prime:
            primes.append(i)

def is_prime(primes, n):
    build_prime(primes, n)

    index = bisect.bisect_left(primes, n)
    if index != len(primes) and primes[index] == n:
        return True

    for j in primes:
        if j > int(math.ceil(math.sqrt(n))) + 1 or j >= n:
            break

        if n % j == 0:
            return False

    return True

nn = int(input())
dp = {}
primes = [2, 3, 5]

build_prime(primes, 26)

for ni in range(0, nn):
    n = int(input())
    count = 0
    for i in range(2, memorize(dp, n) + 1):
        if is_prime(primes, i):
            count += 1

    print(count)

