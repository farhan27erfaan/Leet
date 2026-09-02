# Last updated: 02/09/2026, 11:19:46
1class Solution(object):
2    def largestNumber(self, nums):
3        a = [str(i) for i in nums]
4        a.sort(cmp=lambda x, y: -1 if x + y > y + x else (1 if x + y < y + x else 0))
5        s = "".join(a)
6        while len(s) > 1 and s[0] == '0':
7            s = s[1:]
8        return s