# Last updated: 11/08/2026, 11:39:49
class Solution(object):
    def numOfStrings(self, patterns, word):
      count=0
      for words in patterns:
        if words in word:
            count+=1

       
      return count 