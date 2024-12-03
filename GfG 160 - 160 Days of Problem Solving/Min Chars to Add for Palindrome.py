class Solution:
    def minChar(self, s):
        # Concatenate the string with its reverse and a delimiter
        combined = s + '#' + s[::-1]
        n = len(combined)
        lps = [0] * n
        
        # Build the LPS array
        for i in range(1, n):
            length = lps[i - 1]
            while length > 0 and combined[i] != combined[length]:
                length = lps[length - 1]
            if combined[i] == combined[length]:
                length += 1
            lps[i] = length
        
        # Length of the longest palindrome prefix
        longest_palindrome_prefix = lps[-1]
        return len(s) - longest_palindrome_prefix
