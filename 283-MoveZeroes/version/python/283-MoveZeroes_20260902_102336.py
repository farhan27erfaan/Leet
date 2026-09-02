# Last updated: 02/09/2026, 10:23:36
1
2class Solution(object):
3    def pivotIndex(self, nums):
4    
5        leftSum, rightSum = 0, sum(nums)
6
7        for idx, ele in enumerate(nums):
8            rightSum -= ele
9    
10            if leftSum == rightSum:
11                return idx      
12            leftSum += ele
13        return -1      