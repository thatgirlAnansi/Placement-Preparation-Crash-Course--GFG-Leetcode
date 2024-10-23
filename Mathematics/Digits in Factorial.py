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