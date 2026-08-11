# Last updated: 11/08/2026, 11:40:57
class Solution(object):
    def missingNumber(self, nums):
        nums.sort()
        for i in range(len(nums)):
            if nums[i]!=i:
                return i
            
        return len(nums)

        