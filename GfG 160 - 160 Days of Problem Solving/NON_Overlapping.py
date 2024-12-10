
class Solution:
    def minRemoval(self, intervals):
    # Sort intervals by their end times
        intervals.sort(key=lambda x: x[1])
        
        # Initialize variables
        end = float('-inf')  # End time of the last added interval
        remove_count = 0     # Count of intervals to remove
        
        for interval in intervals:
            if interval[0] < end:  # Overlapping interval
                remove_count += 1
            else:
                end = interval[1]  # Update end to current interval's end
        
        return remove_count
