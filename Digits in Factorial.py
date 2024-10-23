class Solution:
    def digitsInFactorial(self, N):
        def factorial(self, N):
            if N == 0 or N == 1:
                return 1
        
      
        digitsInFactorial = 0
        
       
        result = 1
        for i in range(2, N + 1):
            result *= i
        
    
        while result > 0:
            result = result // 10  
            digitsInFactorial += 1  
        
        return digitsInFactorial



#FASTER APPROACH uses log10 math function
import math

class Solution:
    def digitsInFactorial(self, N: int) -> int:
       
        if N == 0 or N == 1:
            return 1
        
        
        digit_count = 0
        for i in range(1, N + 1):
            digit_count += math.log10(i)
        
        return math.floor(digit_count) + 1
