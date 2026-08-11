# Last updated: 11/08/2026, 11:44:24
class Solution(object):
    def thirdMax(self, nums):
        s=list(set(nums))
       
        s.sort()
        n=len(s)
        if len(s)<3:
            return s[-1]
        else:
            return s[-3]
            


        