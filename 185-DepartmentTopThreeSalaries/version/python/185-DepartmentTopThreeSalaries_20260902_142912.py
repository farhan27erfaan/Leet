# Last updated: 02/09/2026, 14:29:12
1class Solution:
2    def findSecretWord(self, words: List[str], master: 'Master') -> None:
3        freq_at_positions = []
4        for i in range(6):
5            pos_count = {}
6            for word in words:
7                if (word[i] in pos_count): pos_count[word[i]] += 1
8                else: pos_count[word[i]] = 1
9            freq_at_positions.append(pos_count)
10        
11        def calc_score(w):
12            s = 0
13            for i in range(len(w)):
14                s += freq_at_positions[i][w[i]]
15            return s
16
17        words.sort(key=lambda word: calc_score(word))
18
19        def find_common_sum(w1, w2):
20            common_sum = 0
21            for i in range(6):
22                if (w1[i] == w2[i]): common_sum += 1
23            return common_sum
24
25        while (len(words) > 0):
26            word = words.pop()
27            matches = master.guess(word)
28
29            if (matches == 6): break
30            else:
31                words = [w for w in words if matches == find_common_sum(w, word)]