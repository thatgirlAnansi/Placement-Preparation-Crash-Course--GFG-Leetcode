class Solution:
    def nonRepeatingChar(self, s: str) -> str:
        # Dictionary to store the frequency of each character
        char_count = {}
        
        # Loop through each character in the string
        for char in s:
            # Update the frequency count for the character
            # char_count.get(char, 0) -> returns the current count of 'char', or 0 if it's not in the dictionary
            # + 1 increments the count by 1
            char_count[char] = char_count.get(char, 0) + 1
        
        # Loop through the string again to find the first non-repeating character
        for char in s:
            # If the character has a count of 1, it's non-repeating
            if char_count[char] == 1:
                return char
        
        # If no non-repeating character is found, return '$'
        return '$'
