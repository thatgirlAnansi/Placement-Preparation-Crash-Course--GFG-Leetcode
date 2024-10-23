Primality Test
Difficulty: EasyAccuracy: 41.17%Submissions: 106K+Points: 2
A prime number is a number which is only divisible by 1 and itself.
Given number N check if it is prime or not.

 

Example 1:

Input:
N = 5
Output: True
Explanation: 5 is only divisible by 1 
and itself. So, 5 is a prime number.
 

Example 2:

Input:
N = 4
Output: False
Explanation: 4 is divisible by 2. 
So, 4 is not a prime number.
 

Your Task:
You don't need to read input or print anything. Your task is to complete the function isPrime() that takes N as input parameter and returns True if N is prime else returns False. 

 

Expected Time Complexity : O(N1/2)
Expected Auxilliary Space :  O(1)

 

Constraints:
1 <= N <= 109



class Solution:
    def isPrime(self, N):
        if N == 1:
            return False
        if N == 2 or N == 3:
            return True
        if N % 2 == 0 or N % 3 == 0:
            return False
        for i in range(5, int(N**0.5) + 1, 6):
            if N % i == 0 or N % (i + 2) == 0:
                return False
        return True