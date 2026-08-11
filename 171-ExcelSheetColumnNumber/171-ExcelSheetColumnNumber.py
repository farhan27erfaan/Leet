# Last updated: 11/08/2026, 11:41:38
class Solution(object):
    def titleToNumber(self, columnTitle):
        answer=0
        for ch in columnTitle:
            value=ord(ch)-ord('A')+1
            answer=answer*26+value
        return answer

        