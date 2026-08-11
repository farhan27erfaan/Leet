# Last updated: 11/08/2026, 11:41:47
class Solution(object):
    def findMin(self, nums):
        nums.sort()
        return nums[0]  
        