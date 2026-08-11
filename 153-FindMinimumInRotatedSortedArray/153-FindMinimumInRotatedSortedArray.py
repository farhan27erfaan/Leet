# Last updated: 11/08/2026, 11:41:49
"""
class Solution(object):
    def findMin(self, nums):
        n = len(nums)
        for i in range(n):
            for j in range(0, n - i - 1):
                if nums[j] > nums[j + 1]:
                    nums[j], nums[j + 1] = nums[j + 1], nums[j]
        return nums[0]
"""
class Solution(object):
    def findMin(self, nums):
        nums.sort()
        return nums[0]