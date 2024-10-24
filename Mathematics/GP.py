GP Term
Difficulty: EasyAccuracy: 25.04%Submissions: 154K+Points: 2
Given the first 2 terms A and B of a Geometric Series. The task is to find the Nth term of the series.

Example 1:

Input:
A = 2 
B = 3
N = 1
Output: 2
Explanation: The first term is already
given in the input as 2
Example 2:

Input:
A = 1
B = 2
N = 5
Output: 16
Explanation: Common ratio = 2,
Hence Fifth term is 1*(2)(5-1) = 24 = 16 .
Your Task:
You don't need to read input or print anything. Your task is to complete the function termOfGP() that takes A, B and N as parameter and returns Nth term of GP. The return value should be double that would be automatically converted to floor by the driver code.

Expected Time Complexity : O(logN)
Expected Auxilliary Space : O(1)

Constraints:
-100 <= A <= 100
-100 <= B <= 100
1 <= N <= 5

class Solution:    
    def termOfGP(self, A, B, N):
        if N == 1:
            return A
        elif N == 2:
            return B
        
        # Calculate the N-th term using the formula
        r = B / A  # common ratio
        term = A * (r ** (N - 1))
        return term