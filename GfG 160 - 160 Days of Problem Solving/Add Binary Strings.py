class Solution:
    def addBinary(self, s1, s2):
        # Initialize variables
        i, j = len(s1) - 1, len(s2) - 1
        carry = 0
        result = []
        
        # Traverse both strings from the end
        while i >= 0 or j >= 0 or carry:
            bit1 = int(s1[i]) if i >= 0 else 0  # Get bit from s1, or 0 if out of bounds
            bit2 = int(s2[j]) if j >= 0 else 0  # Get bit from s2, or 0 if out of bounds
            
            # Binary addition with carry
            total = bit1 + bit2 + carry
            result.append(str(total % 2))  # Add the result bit (0 or 1)
            carry = total // 2  # Update the carry for the next higher position
            
            # Move to the next digits
            i -= 1
            j -= 1
        
        # Join the result, reverse it, and strip leading zeros
        return ''.join(result[::-1]).lstrip('0') or '0'
