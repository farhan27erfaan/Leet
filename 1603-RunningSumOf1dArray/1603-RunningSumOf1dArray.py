# Last updated: 11/08/2026, 11:40:04
class Solution(object):
    def runningSum(self, nums):
         for i in range(1,len(nums)):
            nums[i]=nums[i]+nums[i-1]
            
         return nums

        