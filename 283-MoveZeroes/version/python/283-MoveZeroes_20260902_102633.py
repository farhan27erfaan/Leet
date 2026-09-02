# Last updated: 02/09/2026, 10:26:33
1import re
2from collections import Counter
3class Solution(object):
4    def mostCommonWord(self, paragraph, banned):
5     
6        banned_set=set(banned)
7        word=re.findall(r'[A-Za-z]+',paragraph)
8        counts=Counter(w.lower() for w in word if w.lower() not in banned_set)
9        return counts.most_common(1)[0][0]
10
11           
12
13
14
15
16        
17        
18        
19        