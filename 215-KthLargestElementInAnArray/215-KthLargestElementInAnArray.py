# Last updated: 11/08/2026, 11:41:16
class Solution:
    def findKthLargest(self, nums, k):
        nums.sort()
        return nums[-k]
