# Last updated: 02/09/2026, 14:23:56
1class Solution:
2    def countDigitOne(self, n: int) -> int:
3        count = 0
4        p = 1  
5        while p <= n:
6            higher = n // (p * 10)
7            current = (n // p) % 10
8            lower = n % p
9
10            if current == 0:
11                count += higher * p
12            elif current == 1:
13                count += higher * p + lower + 1
14            else:
15                count += (higher + 1) * p
16
17            p *= 10
18        return count