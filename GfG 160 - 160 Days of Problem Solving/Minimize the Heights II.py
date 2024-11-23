class Solution:
    def getMinDiff(self, arr, k):
        arr.sort()
        n = len(arr)
        initial_diff = arr[-1] - arr[0]
        min_diff = initial_diff

        for i in range(n - 1):
            high = max(arr[-1] - k, arr[i] + k)
            low = min(arr[0] + k, arr[i + 1] - k)
            if low >= 0:
                min_diff = min(min_diff, high - low)
        
        return min_diff
