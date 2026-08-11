# Last updated: 11/08/2026, 11:41:03
class Solution(object):
    def containsNearbyDuplicate(self, nums, k):
        d = {}

        for i in range(len(nums)):
            if nums[i] in d:
                 if i - d[nums[i]] <= k:
                    return True
            d[nums[i]] = i

        return False
            
            