# Last updated: 02/09/2026, 11:26:37
1class Solution:
2    def maxProduct(self, nums):
3        if not nums:
4            return 0
5            
6        res = max_prod = min_prod = nums[0]
7        
8        for i in range(1, len(nums)):
9            curr = nums[i]
10            
11            if curr < 0:
12                max_prod, min_prod = min_prod, max_prod
13            
14     
15            max_prod = max(curr, curr * max_prod)
16            min_prod = min(curr, curr * min_prod)
17            
18            res = max(res, max_prod)
19            
20        return res