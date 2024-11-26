#dp and Kadane's algo
def circularSubarraySum(arr):
    n = len(arr)
    # Initialize variables
    max_end_here = arr[0]
    min_end_here = arr[0]
    max_so_far = arr[0]
    min_so_far = arr[0]
    total_sum = arr[0]

    for i in range(1, n):
        max_end_here = max(arr[i], max_end_here + arr[i])
        max_so_far = max(max_so_far, max_end_here)

        min_end_here = min(arr[i], min_end_here + arr[i])
        min_so_far = min(min_so_far, min_end_here)

        total_sum += arr[i]

    # Handle circular case
    max_circular = total_sum - min_so_far

    # Handle edge case of all negative elements
    if max_circular == 0:
        return max_so_far

    return max(max_so_far, max_circular)
  
