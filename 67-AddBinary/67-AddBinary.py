# Last updated: 11/08/2026, 11:42:29
class Solution:
    def addBinary(self, a, b):
        return bin(int(a, 2) + int(b, 2))[2:]   