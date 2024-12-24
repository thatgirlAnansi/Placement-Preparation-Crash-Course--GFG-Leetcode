class Solution:

    # Function to search a given number in row-column sorted matrix.
    def searchMatrix(self, mat, x):
        n = len(mat)
        m = len(mat[0])
        
        # Start from the top-right corner of the matrix.
        row, col = 0, m - 1

        while row < n and col >= 0:
            if mat[row][col] == x:
                return True  # Element found
            elif mat[row][col] > x:
                col -= 1  # Move left
            else:
                row += 1  # Move down

        return False  # Element not found
