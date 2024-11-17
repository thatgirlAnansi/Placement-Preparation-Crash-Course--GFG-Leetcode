class Solution:
    # Function to push all zeros to the end
    def pushZerosToEnd(self, arr):
        count = 0  # Keeps track of the position to move non-zero elements
        
        # Traverse the array
        for i in range(len(arr)):
            if arr[i] != 0:
                # Swap elements at index 'i' and 'count'
                arr[i], arr[count] = arr[count], arr[i]
                
                # Increment 'count'
                count += 1
