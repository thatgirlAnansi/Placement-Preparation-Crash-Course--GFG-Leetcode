# Given, N Mice and N holes are placed in a straight line. Each hole can accommodate only 1 mouse. A mouse can stay at his position, move one step right from x to x + 1, or move one step left from x to x-1. Any of these moves consumes 1 minute. Write a program to assign mice to holes so that the time when the last mouse gets inside a hole is minimized.

# Note: Arrays M and H are the positions of the N mice and holes.

# Example 1:

# Input:

# N=3 M = {4, -4, 2)

# H = {4, 0, 5)

# Output: 4

# Explanation:

# If we assign mouse at 1st index to the hole at 1st, mouse at 2nd index to the hole at 2nd and the third to the hole at third. Then, the maximum time taken will be by the 2nd mouse, i.e. 4-0 4 minutes.


# Your Task:

# You don't need to read input or print anything. Your task is to complete the function assignMiceHoles() which takes an Integer N and arrays M and H as input and returns the answer.

# Expected Time Complexity: O(N*log(N))

# Expected Auxiliary Space: O(1)



class Solution:
    def assignMiceHoles(self, N, M, H):
        # Sort the arrays of mice and holes
        M.sort()
        H.sort()
        
        # Initialize a variable to store the maximum time required
        max_time = 0
        
        # Calculate the time each mouse takes to reach the assigned hole
        for i in range(N):
            max_time = max(max_time, abs(M[i] - H[i]))
        
        # Return the maximum time
        return max_time

# Driver Code
if _name_ == '_main_':
    t = int(input())  # Number of test cases
    for _ in range(t):
        N = int(input())  # Number of mice and holes
        M = list(map(int, input().split()))  # Positions of mice
        H = list(map(int, input().split()))  # Positions of holes
        
        # Create an instance of the Solution class
        ob = Solution()
        # Print the result for each test case
        print(ob.assignMiceHoles(N, M, H))
