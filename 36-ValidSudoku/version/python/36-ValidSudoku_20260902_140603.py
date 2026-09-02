# Last updated: 02/09/2026, 14:06:03
1class Solution:
2    def isValidSudoku(self, board: List[List[str]]) -> bool:
3        boardMap = collections.defaultdict(list)
4        for x in range(9):
5            for y in range(9):
6                char = board[x][y]
7                if char != '.': 
8                    if char in boardMap:
9                        for pos in boardMap[char]:
10                            if (pos[0]== x) or (pos[1] == y) or (pos[0]//3 == x//3 and pos[1]//3 == y//3):
11                                return False
12                    boardMap[char].append((x,y))
13   
14        return True