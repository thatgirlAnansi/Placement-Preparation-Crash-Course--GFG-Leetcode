class Solution:

    # Function to search a given number in a row-column sorted matrix.
    def searchRowMatrix(self, mat, x):
        # Get the number of rows and columns
        n = len(mat)
        m = len(mat[0])

        # Iterate over each row in the matrix
        for i in range(n):
            # If x is within the range of the current row, perform a binary search
            if mat[i][0] <= x <= mat[i][-1]:
                left, right = 0, m - 1

                while left <= right:
                    mid = (left + right) // 2

                    # Check if the middle element is the target
                    if mat[i][mid] == x:
                        return True
                    # If the target is greater, move to the right half
                    elif mat[i][mid] < x:
                        left = mid + 1
                    # If the target is smaller, move to the left half
                    else:
                        right = mid - 1

        # If not found, return False
        return False
