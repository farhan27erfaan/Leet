# Last updated: 02/09/2026, 12:09:53
1class Solution(object):
2    def replaceWords(self, dictionary, sentence):
3        result = []
4 
5        roots = set(dictionary)
6        
7        words = sentence.split()
8        for current_word in words:
9            
10            shortest_root = current_word
11            prefix = ""
12         
13            for char in current_word:
14                prefix += char 
15                if prefix in roots:
16                    shortest_root = prefix  
17                    break
18           
19            result.append(shortest_root)
20    
21        return " ".join(result)
22     
23        