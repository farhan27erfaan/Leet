# Last updated: 02/09/2026, 14:10:04
1class Solution:
2    def myAtoi(self, s: str) -> int:
3        s = s.strip()  
4        if not s:
5            return 0
6
7        sign, i, res = 1, 0, 0
8
9        if s[0] == '-':
10            sign = -1
11            i += 1
12        elif s[0] == '+':
13            i += 1
14
15        while i < len(s) and s[i].isdigit():
16            res = res * 10 + int(s[i])
17
18          
19            if sign * res > 2**31 - 1:
20                return 2**31 - 1
21            if sign * res < -2**31:
22                return -2**31
23
24            i += 1
25
26        return sign * res