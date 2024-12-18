class Solution:
    # Function to find the minimum number of pages.
    def findPages(self, arr, k):
        # Helper function to check if allocation is valid
        def is_valid(arr, n, k, max_pages):
            students_required = 1
            current_pages = 0
            
            for pages in arr:
                if current_pages + pages > max_pages:
                    students_required += 1
                    current_pages = pages
                    if students_required > k:  # More students required than allowed
                        return False
                else:
                    current_pages += pages
            
            return True
        
        n = len(arr)
        
        if k > n:  # Not enough books for all students
            return -1
        
        # Initialize binary search bounds
        low, high = max(arr), sum(arr)
        result = -1
        
        while low <= high:
            mid = (low + high) // 2
            if is_valid(arr, n, k, mid):
                result = mid  # Update result to the current mid
                high = mid - 1  # Try for a smaller maximum
            else:
                low = mid + 1  # Increase the maximum
        
        return result
