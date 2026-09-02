# Last updated: 02/09/2026, 10:52:44
1class Solution:
2    def findErrorNums(self, nums):
3        
4        n, a, b = len(nums), sum(nums), sum(set(nums))
5		
6        s = n*(n+1)//2
7        
8        return [a-b, s-b]