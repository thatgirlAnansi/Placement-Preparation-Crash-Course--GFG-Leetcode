class Solution:
    # Function to count inversions in the array.
    def merge_and_count(self, arr, temp_arr, left, mid, right):
        i = left    # Starting index for the left subarray
        j = mid + 1 # Starting index for the right subarray
        k = left    # Starting index to be sorted
        inv_count = 0
        
        # Merge process with inversion counting
        while i <= mid and j <= right:
            if arr[i] <= arr[j]:
                temp_arr[k] = arr[i]
                i += 1
            else:
                temp_arr[k] = arr[j]
                inv_count += (mid - i + 1)  # Count inversions
                j += 1
            k += 1

        # Copy the remaining elements of the left subarray, if any
        while i <= mid:
            temp_arr[k] = arr[i]
            i += 1
            k += 1

        # Copy the remaining elements of the right subarray, if any
        while j <= right:
            temp_arr[k] = arr[j]
            j += 1
            k += 1

        # Copy the sorted subarray into Original array
        for i in range(left, right + 1):
            arr[i] = temp_arr[i]
            
        return inv_count

    def merge_sort_and_count(self, arr, temp_arr, left, right):
        inv_count = 0
        if left < right:
            mid = (left + right) // 2

            # Recursive call to count inversions in the left and right subarrays
            inv_count += self.merge_sort_and_count(arr, temp_arr, left, mid)
            inv_count += self.merge_sort_and_count(arr, temp_arr, mid + 1, right)
            
            # Count inversions during merge
            inv_count += self.merge_and_count(arr, temp_arr, left, mid, right)

        return inv_count

    def inversionCount(self, arr):
        n = len(arr)
        temp_arr = [0] * n
        return self.merge_sort_and_count(arr, temp_arr, 0, n - 1)
