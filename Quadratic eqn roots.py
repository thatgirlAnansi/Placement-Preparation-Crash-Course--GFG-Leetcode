from typing import List
import math

class Solution:
	def quadraticRoots(self, a : int, b : int , c:int ) -> List[int]:
	    D = b * b - 4 * a * c
        

        if D < 0:
            return [-1]
        

        sqrt_D = math.sqrt(D)
        

        root1 = (-b + sqrt_D) / (2 * a)
        root2 = (-b - sqrt_D) / (2 * a)
        

        root1 = math.floor(root1)
        root2 = math.floor(root2)
        
    
        if root1 >= root2:
            return [root1, root2]
        else:
            return [root2, root1]
