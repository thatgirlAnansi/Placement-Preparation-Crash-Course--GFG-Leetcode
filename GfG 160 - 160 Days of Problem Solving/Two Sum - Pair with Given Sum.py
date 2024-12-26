class Solution:
    def twoSum(self, arr, target):
        # Create a set to store numbers we've seen so far
        seen = set()

        # Iterate through the array
        for num in arr:
            # Calculate the complement needed to reach the target
            complement = target - num

            # Check if the complement exists in the set
            if complement in seen:
                return True

            # Add the current number to the set
            seen.add(num)

        # If no pair is found, return False
        return False
