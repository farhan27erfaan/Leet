# Last updated: 02/09/2026, 13:53:57
1class Solution:
2    def isNumber(self, s: str) -> bool:
3        isdot, ise, nums = False, False, False
4        for i, c in enumerate(s):
5            if c.isdigit():
6                nums = True
7            elif c in "+-":
8                if i > 0 and s[i - 1] not in "eE":
9                    return False
10            elif c in "eE":
11                if ise or not nums:
12                    return False
13                ise, nums = True, False
14            elif c == ".":
15                if isdot or ise:
16                    return False
17                isdot = True
18            else:
19                return False
20        return nums