# Last updated: 02/09/2026, 09:59:12
1class Solution(object):
2    def matrixReshape(self, mat, r, c):
3        m, n = len(mat), len(mat[0])
4        if m * n != r * c:
5            return mat
6        
7        flat = [num for row in mat for num in row]
8        return [flat[i * c:(i + 1) * c] for i in range(r)]