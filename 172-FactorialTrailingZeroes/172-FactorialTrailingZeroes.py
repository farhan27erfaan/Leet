# Last updated: 11/08/2026, 11:41:35
class Solution(object):
    def trailingZeroes(self, n):
        count = 0
        divisor = 5

        while n >= divisor:
            count += n // divisor
            divisor *= 5

        return count
        