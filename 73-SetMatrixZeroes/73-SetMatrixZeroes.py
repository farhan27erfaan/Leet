# Last updated: 11/08/2026, 11:42:21
class Solution:
    def setZeroes(self, matrix):
        rows = set()
        cols = set()

        m = len(matrix)
        n = len(matrix[0])

        
        for i in range(m):
            for j in range(n):
                if matrix[i][j] == 0:
                    rows.add(i)
                    cols.add(j)

        
        for i in range(m):
            for j in range(n):
                if i in rows or j in cols:
                    matrix[i][j] = 0