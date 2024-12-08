def merge_intervals_stack(arr):
    # Step 1: Sort the intervals by the start time
    arr.sort(key=lambda x: x[0])
    
    # Step 2: Initialize a stack
    stack = []
    
    for interval in arr:
        # Step 3: If the stack is empty or no overlap, push the interval
        if not stack or stack[-1][1] < interval[0]:
            stack.append(interval)
        else:
            # Step 4: Merge the intervals
            stack[-1][1] = max(stack[-1][1], interval[1])
    
    return stack
