class Solution:
    def kthMissing(self, arr, k):
        # Initialize a pointer for the array and a counter for missing numbers
        pointer = 0
        current = 1

        # Traverse until we find the kth missing number
        while k > 0:
            if pointer < len(arr) and arr[pointer] == current:
                # If the current number exists in the array, move the pointer
                pointer += 1
            else:
                # If the current number is missing, decrease k
                k -= 1

            # Increment the current number
            current += 1

        # Return the last number checked, which is the kth missing number
        return current - 1
