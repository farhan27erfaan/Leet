# Last updated: 11/08/2026, 11:41:01
class Solution:
    def isPowerOfTwo(self, n: int) -> bool:
        return n > 0 and not (n & (n - 1))