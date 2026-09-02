# Last updated: 02/09/2026, 14:01:17
1class Solution(object):
2    def myAtoi(self, s):
3    
4        i = 0
5        n = len(s)
6        
7        while i < n and s[i] == ' ':
8            i += 1
9        
10        sign = 1
11        if i < n and (s[i] == '-' or s[i] == '+'):
12            sign = -1 if s[i] == '-' else 1
13            i += 1
14        
15        result = 0
16        while i < n and s[i].isdigit():
17            result = result * 10 + int(s[i])
18            if result * sign > 2**31 - 1:
19                return 2**31 - 1
20            if result * sign < -2**31:
21                return -2**31
22            i += 1
23        
24        return result * sign