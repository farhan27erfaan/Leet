# Last updated: 02/09/2026, 11:41:09
1class Solution(object):
2    def maxProfit(self, prices):
3        max = 0
4        start = prices[0]
5        len1 = len(prices)
6        for i in range(0 , len1):
7            if start < prices[i]: 
8                max += prices[i] - start
9            start = prices[i]
10        return max