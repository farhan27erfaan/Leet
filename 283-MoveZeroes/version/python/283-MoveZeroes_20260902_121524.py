# Last updated: 02/09/2026, 12:15:24
1class Solution:
2    mInf = float('-inf')
3    def largestSumOfAverages(self, A, K):
4        mInf  = self.mInf
5        L    = len(A)
6        memo = {}
7        def dfs(i,n):
8            if (n<=0) or (i>=L):
9                return 0 if (i==L and not n) else mInf
10            if (i,n) in memo:
11                return memo[i,n]
12            best = mInf
13            
14            if n>=(L-i) or n==1:
15                if n==(L-i):
16                    memo[i,n] = best = sum(A[i:])
17                elif n==1:
18                    memo[i,n] = best = sum(A[i:])/float(L-i)
19                return best
20          
21            s    = 0
22            for j in range(i,L):
23                s    += A[j]
24                new   = s/(j-i+1.) + dfs(j+1,n-1)
25                if new == mInf: break
26                best  = max(best, new )
27            memo[i,n] = best
28            return best
29        return dfs(0,K)