# Last updated: 02/09/2026, 12:28:25
1class Solution:
2    def longestPalindrome(self, s):
3
4
5        def expand_around_center(s,left,right):
6            while left >= 0 and right < len(s) and s[left] == s[right]:
7                left -= 1
8                right += 1
9            return right - left - 1
10
11
12        start = 0
13        end = 0
14
15        for i in range(len(s)):
16            odd = expand_around_center(s, i, i)
17            even = expand_around_center(s, i, i + 1)
18            max_len = max(odd, even)
19            
20            if max_len > end - start:
21                start = i - (max_len - 1) // 2
22                end = i + max_len // 2
23        
24        return s[start:end+1]