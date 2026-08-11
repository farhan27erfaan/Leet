# Last updated: 11/08/2026, 11:40:46
class Solution(object):
    def fizzBuzz(self, n):
            result =[]
    
            for i in range(1,n+1):
                if i%3==0 and i%5==0 :
                    result.append("FizzBuzz")
                elif i%3==0:
                    result.append("Fizz")
                elif i%5==0:
                    result.append("Buzz")
                else:
                    result.append(str(i))
        
            return result
        

    