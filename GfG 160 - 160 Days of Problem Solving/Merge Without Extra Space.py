class Solution:
    def mergeArrays(self, a, b):
        n, m = len(a), len(b)
        gap = (n + m + 1) // 2  # Initial gap calculation

        while gap > 0:
            i = 0
            j = gap

            # Compare elements in a[]
            while j < n:
                if a[i] > a[j]:
                    a[i], a[j] = a[j], a[i]
                i += 1
                j += 1

            # Compare elements between a[] and b[]
            j = gap - n if gap > n else 0
            while i < n and j < m:
                if a[i] > b[j]:
                    a[i], b[j] = b[j], a[i]
                i += 1
                j += 1

            # Compare elements in b[]
            i = 0
            while j < m:
                if b[i] > b[j]:
                    b[i], b[j] = b[j], b[i]
                i += 1
                j += 1

            # Reduce the gap
            if gap == 1:
                break
            gap = (gap + 1) // 2
