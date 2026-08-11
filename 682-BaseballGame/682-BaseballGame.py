# Last updated: 11/08/2026, 11:40:35
class Solution(object):
    def calPoints(self, operations):
        stack=[]
        for op in operations:


            if op=='+':
                stack.append(stack[-2]+stack[-1])
            elif op=='D':
                stack.append(2*stack[-1])
            elif op=='C':
                stack.pop()
            else:
                stack.append(int(op))
        return sum(stack)



        