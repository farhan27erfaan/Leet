# Last updated: 11/08/2026, 11:42:41
"""
class Solution(object):
    def myPow(self, x, n):

        if n==0:
            return 1

        if n<0:
            x=1/x
            n=-n

        ans=1


        for i in range(n):
            ans*=x
        
        return  ans
"""
class Solution:
    def myPow(self, x, n):
        if n < 0:
            x = 1 / x
            n = -n

        ans = 1

        while n > 0:
            if n % 2 == 1:
                ans *= x

            x *= x
            n //= 2

        return ans