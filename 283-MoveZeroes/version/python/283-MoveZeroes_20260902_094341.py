# Last updated: 02/09/2026, 09:43:41
1class Solution:
2    def moveZeroes(self, nums):
3        j = 0
4        for i in range(len(nums)):
5            if nums[i] != 0:
6                
7                nums[i], nums[j] = nums[j], nums[i]
8                j += 1 
9