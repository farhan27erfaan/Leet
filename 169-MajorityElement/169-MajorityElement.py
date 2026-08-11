# Last updated: 11/08/2026, 11:41:42
class Solution(object):
    def majorityElement(self, nums):
        nums.sort()
        return nums[(len(nums)//2)]
