# Last updated: 11/08/2026, 11:39:30


class Solution(object):
    def isPossibleToSplit(self, nums):
        count = Counter(nums)

        for value in count.values():
            if value > 2:
                return False

        return True