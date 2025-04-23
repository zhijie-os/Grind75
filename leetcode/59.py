# 59. Spiral Matrix II
class Solution:
    def generateMatrix(self, n: int) -> List[List[int]]:
        matrix = [[-1 for _ in range(n)] for _ in range(n)]
        top = 0
        bottom = n - 1
        left = 0
        right = n - 1

        dir = 0
        c = 1
        while top != bottom or left != right:
            if dir % 4 == 0:
                for j in range(left, right+1): # inclusive on the right
                    matrix[top][j] = c
                    c += 1
                top += 1
            elif dir % 4 == 1:
                for i in range(top, bottom + 1):
                    matrix[i][right] = c
                    c += 1
                right -= 1
            elif dir % 4 == 2:
                for j in range(right, left - 1, -1):
                    matrix[bottom][j] = c
                    c += 1
                bottom -= 1
            else:
                for i in range(bottom, top - 1, -1):
                    matrix[i][left] = c
                    c += 1
                left += 1
            dir += 1
        matrix[top][left] = c
        return matrix
