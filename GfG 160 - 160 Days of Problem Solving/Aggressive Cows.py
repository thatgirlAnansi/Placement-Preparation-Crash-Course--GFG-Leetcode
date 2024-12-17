class Solution:
    def aggressiveCows(self, stalls, k):
        # Step 1: Sort the stalls
        stalls.sort()
        
        # Helper function to check if we can place cows with minimum distance 'mid'
        def canPlaceCows(mid):
            cows_count = 1  # First cow is placed at the first stall
            last_position = stalls[0]
            
            for i in range(1, len(stalls)):
                if stalls[i] - last_position >= mid:
                    cows_count += 1
                    last_position = stalls[i]
                    if cows_count >= k:  # All cows have been placed successfully
                        return True
            return False
        
        # Step 2: Binary search on the minimum distance
        low = 1
        high = stalls[-1] - stalls[0]
        result = 0
        
        while low <= high:
            mid = (low + high) // 2
            if canPlaceCows(mid):
                result = mid  # Update the result
                low = mid + 1  # Try for a larger minimum distance
            else:
                high = mid - 1  # Reduce the minimum distance
        
        return result
