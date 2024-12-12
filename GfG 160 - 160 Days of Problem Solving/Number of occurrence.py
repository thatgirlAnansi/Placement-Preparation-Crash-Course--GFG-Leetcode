import bisect

class Solution:
    def countFreq(self, arr, target):
        # Find the first and last index of the target using binary search
        first = bisect.bisect_left(arr, target)  # First occurrence
        last = bisect.bisect_right(arr, target)  # One position after the last occurrence
        
        # If the target is not found, first will equal last
        if first == last:
            return 0
        
        # The number of occurrences is the difference between last and first
        return last - first
