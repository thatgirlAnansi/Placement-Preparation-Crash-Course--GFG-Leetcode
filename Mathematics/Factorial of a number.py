Factorial Of Number
Difficulty: EasyAccuracy: 62.28%Submissions: 66K+Points: 2
Given a positive integer N. The task is to find factorial of N.

Example 1:

Input:
N = 4
Output: 24
Explanation: 4! = 4 * 3 * 2 * 1 = 24
Example 2:

Input:
N = 13
Output: 6227020800
Explanation: 
13! = 13 * 12 * .. * 1 = 6227020800
Your Task:
You don't need to read input or print anything. Your task is to complete the function factorial() that takes N as parameter and returns factorial of N.

Expected Time Complexity : O(N)
Expected Auxilliary Space : O(1)

Constraints:
0 <= N <= 18


class Solution:
    #You need to complete this function
    def factorial(self,N):
        if N == 0 or N == 1:
            return 1

        result = 1

        for i in range(2, N + 1):
            result *= i
        
        return result