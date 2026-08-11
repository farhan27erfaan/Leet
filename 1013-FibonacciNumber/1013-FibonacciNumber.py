# Last updated: 11/08/2026, 11:40:22
class Solution(object):
    def fib(self, n):
        a,b=0,1
        for i in range(n):
            a,b=b,a+b
        return a

        