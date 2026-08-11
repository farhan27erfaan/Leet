# Last updated: 11/08/2026, 11:39:28
class Solution(object):
    def sumAndMultiply(self, n):
        s = str(n)
        con = ""
        summ = 0

        for ch in s:
            summ += int(ch)

            if ch != '0':
                con += ch

        if con == "":
            con = "0"

        return int(con) * summ
        
                

        