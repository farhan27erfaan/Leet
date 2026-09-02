# Last updated: 02/09/2026, 11:12:41
1class Solution:
2    def removeDuplicates(self, nums):
3        j = 1
4        for i in range(1, len(nums)):
5            if j == 1 or nums[i] != nums[j - 2]:
6                nums[j] = nums[i]
7                j += 1
8        return j