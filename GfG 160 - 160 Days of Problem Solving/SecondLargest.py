class Solution:
    def getSecondLargest(self, arr):
        n = len(arr)
        
        # Edge case: If there are fewer than 2 elements
        if n < 2:
            return -1
        
        res = -1  # To store the index of second largest
        largest = 0  # Initially, assume the first element is the largest
        
        for i in range(1, n):
            # If current element is greater than the largest
            if arr[i] > arr[largest]:
                res = largest
                largest = i
            # If current element is not equal to largest and is greater than the current second largest
            elif arr[i] != arr[largest]:
                if res == -1 or arr[i] > arr[res]:
                    res = i

        return arr[res] if res != -1 else -1  # Return second largest value, or -1 if not found
