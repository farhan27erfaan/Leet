# Last updated: 02/09/2026, 14:21:33
1class Solution:
2    def calculate(self, s: str) -> int:
3        num = 0
4        sign = 1
5        res = 0
6        stack = []
7        for i in range(len(s)): 
8            c = s[i]
9            if c.isdigit(): 
10                num = num*10 + int(c) 
11            elif c in '-+': 
12                res += num*sign
13                sign = -1 if c == '-' else 1
14                num = 0
15            elif c == '(':
16                stack.append(res)
17                stack.append(sign)
18                res = 0
19                sign = 1
20            elif c == ')':
21                res +=sign*num
22                res *=stack.pop()
23                res +=stack.pop()
24                num = 0
25        return res + num*sign