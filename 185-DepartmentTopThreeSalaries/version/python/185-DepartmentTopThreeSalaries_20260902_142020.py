# Last updated: 02/09/2026, 14:20:20
1class Solution:
2  
3    map = {}
4
5    def isScramble(self, s1: str, s2: str) -> bool:
6        n = len(s1)
7
8        if s1 == s2:
9            return True
10       
11        a, b, c = [0] * 26, [0] * 26, [0] * 26
12      
13        if (s1 + s2) in self.map:
14            return self.map[s1 + s2]
15       
16        for i in range(1, n):
17            j = n - i
18            
19            a[ord(s1[i - 1]) - ord('a')] += 1
20            b[ord(s2[i - 1]) - ord('a')] += 1
21            c[ord(s2[j]) - ord('a')] += 1
22          
23            if a == b and self.isScramble(s1[:i], s2[:i]) and self.isScramble(s1[i:], s2[i:]):
24               
25                self.map[s1 + s2] = True
26                return True
27           
28            if a == c and self.isScramble(s1[:i], s2[j:]) and self.isScramble(s1[i:], s2[:j]):
29               
30                self.map[s1 + s2] = True
31                return True
32      
33        self.map[s1 + s2] = False
34        return False