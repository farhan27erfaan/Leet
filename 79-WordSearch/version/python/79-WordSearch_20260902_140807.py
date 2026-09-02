# Last updated: 02/09/2026, 14:08:07
1class Solution:
2    def groupAnagrams(self, strs):
3        anagram_map = defaultdict(list)
4        
5        for word in strs:
6            sorted_word = ''.join(sorted(word))
7            anagram_map[sorted_word].append(word)
8        
9        return list(anagram_map.values())