# Last updated: 02/09/2026, 10:48:20
1class Solution(object):
2    def isMonotonic(self, nums):
3        increasing = True
4        decreasing = True
5
6        for i in range(len(nums) - 1):
7
8            if nums[i] > nums[i + 1]:
9                increasing = False
10
11            if nums[i] < nums[i + 1]:
12                decreasing = False
13
14        return increasing or decreasing