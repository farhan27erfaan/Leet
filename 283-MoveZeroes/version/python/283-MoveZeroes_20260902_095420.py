# Last updated: 02/09/2026, 09:54:20
1class Solution(object):
2    def arrayPairSum(self, nums):
3        nums.sort()
4        total=0
5        for i in range(0,len(nums),2):
6            total+=min(nums[i],nums[i+1])
7        return total
8
9        