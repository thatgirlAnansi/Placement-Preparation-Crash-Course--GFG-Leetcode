Exactly 3 Divisors
Difficulty: EasyAccuracy: 22.85%Submissions: 120K+Points: 2
Given a positive integer value n. The task is to find how many numbers less than or equal to n have numbers of divisors exactly equal to 3.

Examples:

Input: n = 6
Output: 1
Explanation: The only number less than 6 with 3 divisors is 4 which has 1, 2 and 4 as divisors.
Input: n = 10
Output: 2
Explanation: 4 and 9 have 3 divisors.
Your Task:
You don't need to read input or print anything. Your task is to complete the function exactly3Divisors() that takes n as input parameter and returns count of numbers less than or equal to n with exactly 3 divisors.

Expected Time Complexity : O(n1/2 * n1/4)
Expected Auxilliary Space :  O(1)

Constraints :
1 <= n <= 109


class Solution:
    def sieve_of_eratosthenes(self, N):
        is_prime = [True] * (N + 1)
        is_prime[0] = is_prime[1] = False
        
        for i in range(2, int(N ** 0.5) + 1):
            if is_prime[i]:
                for j in range(i * i, N + 1, i):
                    is_prime[j] = False
        
        primes = []
        for i in range(2, N + 1):
            if is_prime[i]:
                primes.append(i)
        
        return primes
    
    def exactly3Divisors(self, N):
        limit = int(math.sqrt(N))
        primes = self.sieve_of_eratosthenes(limit)
        
        count = 0
        for prime in primes:
            if prime * prime <= N:
                count += 1
            else:
                break
                
        return count