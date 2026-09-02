# Last updated: 02/09/2026, 14:25:20
1class Solution:
2    def numberToWords(self, num: int) -> str:
3        if num == 0:
4            return "Zero"
5
6        units = {
7            1: "One", 2: "Two", 3: "Three", 4: "Four", 5: "Five", 
8            6: "Six", 7: "Seven", 8: "Eight", 9: "Nine", 10: "Ten",
9            11: "Eleven", 12: "Twelve", 13: "Thirteen", 14: "Fourteen",
10            15: "Fifteen", 16: "Sixteen", 17: "Seventeen", 18: "Eighteen",
11            19: "Nineteen"
12        }
13
14        tens = {
15            2: "Twenty", 3: "Thirty", 4: "Forty", 5: "Fifty", 
16            6: "Sixty", 7: "Seventy", 8: "Eighty", 9: "Ninety"
17        }
18
19        def getHundred(num):
20            result = []
21            if num >= 100:
22                n = num // 100
23                result.append(units[n] + " Hundred")
24                num %= 100
25            if num >= 20:
26                n = num // 10
27                result.append(tens[n])
28                num %= 10
29            if num > 0:
30                result.append(units[num])
31            return " ".join(result)
32
33        answer = []
34        if num >= 1e9:
35            n = num // 1e9
36            answer.append(getHundred(n) + " Billion")
37            num %= 1e9
38        if num >= 1e6:
39            n = num // 1e6
40            answer.append(getHundred(n) + " Million")
41            num %= 1e6
42        if num >= 1e3:
43            n = num // 1e3
44            answer.append(getHundred(n) + " Thousand")
45            num %= 1e3
46        answer.append(getHundred(num))
47
48        return " ".join(answer).strip()
49