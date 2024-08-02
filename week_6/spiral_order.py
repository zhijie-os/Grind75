class Solution:
    def spiralOrder(self, matrix: List[List[int]]) -> List[int]:
        if len(matrix) == 0:
            return []

        m = len(matrix)
        n = len(matrix[0])

        top = 0
        bottom = m - 1
        left = 0
        right = n - 1

        result = []
        while top <= bottom and left <= right:
            
            # iterate the top row
            for i in range(left, right+1):
                result.append(matrix[top][i])
            top += 1
            if not (top <= bottom and left <= right):
                break

            # iterate the right column
            for i in range(top, bottom+1):
                result.append(matrix[i][right])
            right -= 1
            if not (top <= bottom and left <= right):
                break

            # iterate the bottom row
            for i in range(right, left - 1 , -1):
                result.append(matrix[bottom][i])
            bottom -= 1
            if not (top <= bottom and left <= right):
                break

            # iterate the left column
            for i in range(bottom, top - 1, -1):
                result.append(matrix[i][left])
            left += 1
            if not (top <= bottom and left <= right):
                break
        return result