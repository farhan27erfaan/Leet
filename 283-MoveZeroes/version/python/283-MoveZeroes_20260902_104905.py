# Last updated: 02/09/2026, 10:49:05
1class Solution(object):
2    def findShortestSubArray(self, nums):
3        count = {}
4        left = {}
5        right = {}
6        for i, num in enumerate(nums):
7            count[num] = count.get(num, 0) + 1
8            if num not in left:
9                left[num] = i
10            right[num] = i
11        degree = max(count.values())
12        res = float('inf')
13        for num in count:
14            if count[num] == degree:
15                res = min(res, right[num] - left[num] + 1)
16        return res