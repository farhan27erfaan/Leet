# Last updated: 11/08/2026, 11:42:43
class Solution:
    def firstMissingPositive(self, nums):
        s = set(nums)

        i = 1
        while True:
            if i not in s:
                return i
            i += 1
        