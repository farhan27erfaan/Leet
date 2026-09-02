# Last updated: 02/09/2026, 14:14:21
1class Solution(object):
2    def candy(self, ratings):
3        """
4        :type ratings: List[int]
5        :rtype: int
6        """
7        n = len(ratings)
8        candies = [1] * n  
9
10      
11        for i in range(1, n):
12            if ratings[i] > ratings[i - 1]:
13                candies[i] = candies[i - 1] + 1
14
15      
16        for i in range(n - 2, -1, -1):
17            if ratings[i] > ratings[i + 1]:
18                candies[i] = max(candies[i], candies[i + 1] + 1)
19
20      
21        return sum(candies)