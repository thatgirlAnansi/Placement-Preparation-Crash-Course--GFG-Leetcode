
Quadratic Equation Roots
Difficulty: BasicAccuracy: 12.78%Submissions: 232K+Points: 1
Given a quadratic equation ax2 + bx + c = 0, find its roots. If the roots are imaginary, return only one integer -1. Always return the roots as the greatest integers less than or equal to the actual roots, with the maximum root first followed by the minimum root.

Note: If roots are imaginary, the generated output will display "Imaginary".

Examples:

Input:
a = 1, b = -2, c = 1
Output: 1 1
Explanation:
Roots of equation x2-2x+1 are 1 and 1.
Input:
a = 1, b = -7, c = 12
Output: 4 3
Explanation: Roots of equation x2 - 7x + 12 are 4 and 3.
 

Expected Time Complexity: O(1)
Expected Auxiliary Space : O(1)

 

Constraints:
-103 <= a,b,c <= 103





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