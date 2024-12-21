class Solution:
    # Function to return a list of integers denoting spiral traversal of matrix.
    def spirallyTraverse(self, mat):
        # Initialize boundaries
        top, bottom, left, right = 0, len(mat) - 1, 0, len(mat[0]) - 1
        result = []

        while top <= bottom and left <= right:
            # Traverse from left to right on the current top row
            for i in range(left, right + 1):
                result.append(mat[top][i])
            top += 1

            # Traverse from top to bottom on the current right column
            for i in range(top, bottom + 1):
                result.append(mat[i][right])
            right -= 1

            if top <= bottom:
                # Traverse from right to left on the current bottom row
                for i in range(right, left - 1, -1):
                    result.append(mat[bottom][i])
                bottom -= 1

            if left <= right:
                # Traverse from bottom to top on the current left column
                for i in range(bottom, top - 1, -1):
                    result.append(mat[i][left])
                left += 1

        return result
