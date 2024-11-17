from itertools import permutations

class Solution:
    def findPermutation(self, s):
        # Generate all permutations using itertools
        perm = permutations(s)
        
        # Use a set to store unique permutations
        unique_permutations = set(perm)
        
        # Convert each tuple back to string, sort them lexicographically
        sorted_permutations = sorted("".join(p) for p in unique_permutations)
        
        return sorted_permutations
