Modular Multiplicative Inverse
Difficulty: EasyAccuracy: 43.0%Submissions: 80K+Points: 2
Given two integers ‘a’ and ‘m’. The task is to find the smallest modular multiplicative inverse of ‘a’ under modulo ‘m’. if it does not exist then return -1.

 

Example 1:

Input:
a = 3
m = 11
Output: 4
Explanation: Since (4*3) mod 11 = 1, 4 
is modulo inverse of 3. One might think,
15 also as a valid output as "(15*3)
mod 11"  is also 1, but 15 is not in 
ring {0, 1, 2, ... 10}, so not valid.
 

Example 2:

Input:
a = 10
m = 17
Output: 12
Explanation: Since (12*10) mod 17 = 1,
12 is the modulo inverse of 10.
 

Your Task:
You don't need to read input or print anything. Your task is to complete the function function modInverse() that takes a and m as input parameters and returns modular multiplicative inverse of ‘a’ under modulo ‘m’. If the modular multiplicative inverse doesn't exist return -1.

 

Expected Time Complexity : O(m)
Expected Auxilliary Space : O(1)

 

Constraints:
1 <= a <= 104
1 <= m <= 104




class Solution:    

    def modInverse(self,a,m):
        for x in range(1, m):
            if (a * x) % m == 1:
                return x

        return -1




