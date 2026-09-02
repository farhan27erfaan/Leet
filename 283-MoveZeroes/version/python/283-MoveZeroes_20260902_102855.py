# Last updated: 02/09/2026, 10:28:55
1class Solution:
2    def sortArrayByParity(self, nums: List[int]) -> List[int]:
3        nums[:] = [i for i in nums if i%2==0] + [j for j in nums if j%2!=0]
4        return nums