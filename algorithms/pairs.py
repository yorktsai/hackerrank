# https://www.hackerrank.com/challenges/pairs

import bisect

n, k = list(map(int, input().split()))
nums = list(map(int, input().split()))

count = 0
nums.sort()
for i in range(0, n):
    index = bisect.bisect_left(nums, k+nums[i], i+1, n)
    if index != len(nums) and nums[index] == k+nums[i]:
        count += 1

print(count)
