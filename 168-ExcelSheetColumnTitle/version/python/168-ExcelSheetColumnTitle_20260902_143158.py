# Last updated: 02/09/2026, 14:31:58
1class Solution:
2    def convertToTitle(self, columnNumber: int) -> str:
3        result = ""
4        while columnNumber > 0:
5            index = (columnNumber - 1) % 26
6            result = chr(index + ord('A')) + result
7            columnNumber = (columnNumber - 1) // 26
8        return result