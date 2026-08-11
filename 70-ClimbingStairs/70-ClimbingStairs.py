# Last updated: 11/08/2026, 11:42:24
class Solution:
    def climbStairs(self, n):
        p2, p1 = 0, 1
        for i in range(n):
            p2, p1 = p1, (p1+p2)
        return p1