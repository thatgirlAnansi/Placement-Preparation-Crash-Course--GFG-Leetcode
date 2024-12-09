def insert(intervals, newInterval):
    result = []
    i = 0
    n = len(intervals)

    # Add all intervals that end before the new interval starts
    while i < n and intervals[i][1] < newInterval[0]:
        result.append(intervals[i])
        i += 1
    
    # Merge all intervals that overlap with the new interval
    while i < n and intervals[i][0] <= newInterval[1]:
        newInterval[0] = min(newInterval[0], intervals[i][0])
        newInterval[1] = max(newInterval[1], intervals[i][1])
        i += 1
    
    # Add the merged new interval
    result.append(newInterval)
    
    # Add all intervals that start after the new interval ends
    while i < n:
        result.append(intervals[i])
        i += 1
    
    return result
