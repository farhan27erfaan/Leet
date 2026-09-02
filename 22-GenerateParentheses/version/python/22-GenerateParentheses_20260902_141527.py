# Last updated: 02/09/2026, 14:15:27
1class Solution:
2    def canCross(self, stones: List[int]) -> bool:
3        m = {}  
4        n = len(stones)
5        dp = [[-1] * n for _ in range(n)]
6
7        def solve(i, k):
8            if i == n - 1:
9                return True
10
11            if dp[i][k] != -1:
12                return dp[i][k] == 1
13
14            k0, kp, k1 = False, False, False
15
16            if stones[i] + k in m:
17                k0 = solve(m[stones[i] + k], k)
18            if k > 1 and stones[i] + k - 1 in m:
19                kp = solve(m[stones[i] + k - 1], k - 1)
20            if stones[i] + k + 1 in m:
21                k1 = solve(m[stones[i] + k + 1], k + 1)
22
23            dp[i][k] = 1 if k0 or kp or k1 else 0
24            return dp[i][k] == 1
25
26        if stones[1] - stones[0] != 1:
27            return False
28
29        for i in range(n):
30            m[stones[i]] = i
31
32        return solve(1, 1)