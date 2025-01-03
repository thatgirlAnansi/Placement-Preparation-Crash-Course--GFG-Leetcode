# Given an even number n (greater than 2), retum two prime numbers whose sum will be equal to the given number. There are several combinations possible. Print only the pair whose minimum value is the smallest among all the minimum values of pairs and print the minimum element first.

# NOTE: A solution will always exist, read Goldbach's conjecture.

# Example 1:

# Input: n = 74

# Output: 3 71

# Explaination: There are several possibilities like 37 37. But the minimum value of this pair is 3 which is smallest among all possible minimum values of all the pairs.

# Example 2:

# Input: n = 4

# Output: 22

# Explaination: This is the only possible

# prtitioning of 4.

# Your Task:

# You do not need to read input or print anything. Your task is to complete the function primeDivision() which takes n as input parameter and returns the partition satisfying the condition.
# Expected Time Complexity: O(N*log(logN)) Expected Auxiliary Space: O(N)

# Constraints: 4≤n≤104

# #User function Template for python3

# class Solution:

# def primeDivision(self, n): # code here

# #{

# #Driver Code Starts

# #Initial Template for Python 3

# if name == main_':

# t = int(input()) for in range(t): N = int(input())

# ob = Solution()

# p1, p2 = ob.primeDivision(N)

# print(p1, end = ")

# print(p2)

# #} Driver Code Ends



class Solution:
    def primeDivision(self, n):
        # Sieve of Eratosthenes to find all primes up to n
        is_prime = [True] * (n + 1)
        is_prime[0] = is_prime[1] = False  # 0 and 1 are not prime numbers
        
        for i in range(2, int(n**0.5) + 1):
            if is_prime[i]:
                for j in range(i * i, n + 1, i):
                    is_prime[j] = False
        
        # List of all prime numbers less than or equal to n
        primes = [i for i in range(n + 1) if is_prime[i]]

        # Finding the pair of primes
        for prime in primes:
            complement = n - prime
            if complement >= 0 and is_prime[complement]:
                return (min(prime, complement), max(prime, complement))

# Driver Code
if _name_ == "_main_":
    t = int(input())
    for _ in range(t):
        N = int(input())
        ob = Solution()
        p1, p2 = ob.primeDivision(N)
        print(p1, p2)
