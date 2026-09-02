# Last updated: 02/09/2026, 14:09:15
1class Solution:
2    def countAndSay(self, n: int) -> str:
3        result = "1"
4        for _ in range(n - 1):
5            result = self.describe(result)
6        return result
7
8    def describe(self, s: str) -> str:
9        result = []
10        count = 1
11
12        for i in range(1, len(s)):
13            if s[i] == s[i - 1]:
14                count += 1
15            else:
16                result.append(f"{count}{s[i - 1]}")
17                count = 1
18
19        result.append(f"{count}{s[-1]}")
20        return "".join(result)