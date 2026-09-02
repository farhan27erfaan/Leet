# Last updated: 02/09/2026, 14:23:00
1class Solution:
2    def poorPigs(self, buckets: int, timeDetect: int, timeTest: int) -> int:
3        return ceil(log2(buckets)/log2(timeTest//timeDetect+1))
4        