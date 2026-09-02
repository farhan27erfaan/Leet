# Last updated: 02/09/2026, 11:11:31
1class Solution:
2    def canJump(self, nums):
3        m = 0
4        for i, n in enumerate(nums):
5            if i > m:
6                return False
7            m = max(m, i+n)
8        return True