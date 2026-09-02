# Last updated: 02/09/2026, 14:26:45
1class Solution:
2    def addOperators(self, s: str, target: int) -> List[str]:
3        
4        res = []
5
6        def dfs(i, path, cur_num, prevNum):
7            if i == len(s):
8                if cur_num == target:
9                    res.append(path)
10                return
11            
12            for j in range(i, len(s)):
13                
14                if j > i and s[i] == '0':
15                    break
16                num = int(s[i:j+1])
17
18                if i == 0:
19                    dfs(j + 1, path + str(num), cur_num + num, num)
20                else:
21                    dfs(j + 1, path + "+" + str(num), cur_num + num, num)
22                    dfs(j + 1, path + "-" + str(num), cur_num - num, -num)
23                    dfs(j + 1, path + "*" + str(num), cur_num - prevNum + prevNum * num, prevNum * num)
24        
25        dfs(0, "", 0, 0)
26        return res
27        