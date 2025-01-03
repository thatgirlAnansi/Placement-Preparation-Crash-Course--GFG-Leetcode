class Solution:
    def find(self, arr, x):
        def binary_search_first(arr, x):
            low, high = 0, len(arr) - 1
            result = -1
            while low <= high:
                mid = (low + high) // 2
                if arr[mid] == x:
                    result = mid
                    high = mid - 1  # Move to the left half
                elif arr[mid] < x:
                    low = mid + 1
                else:
                    high = mid - 1
            return result

        def binary_search_last(arr, x):
            low, high = 0, len(arr) - 1
            result = -1
            while low <= high:
                mid = (low + high) // 2
                if arr[mid] == x:
                    result = mid
                    low = mid + 1  # Move to the right half
                elif arr[mid] < x:
                    low = mid + 1
                else:
                    high = mid - 1
            return result

        first_index = binary_search_first(arr, x)
        last_index = binary_search_last(arr, x)

        # If the element is not found, both indices should be -1
        if first_index == -1:
            return [-1, -1]
        
        return [first_index, last_index]
