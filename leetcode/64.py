# 64. Minimum Path Sum
class Solution:
    def minPathSum(self, grid: List[List[int]]) -> int:
        visited = [[False for _ in range(len(grid[0]))] for _ in range(len(grid))]
        dp = [[-1 for _ in range(len(grid[0]))] for _ in range(len(grid))]
        return self.dfs(grid, visited, 0, 0, dp)

    def dfs(self, grid, visited, i, j, dp):
        if i == len(grid) - 1 and j == len(grid[0]) - 1:
            dp[i][j] = grid[i][j]
            return grid[i][j]

        if visited[i][j]:
            return sys.maxsize

        if dp[i][j] != -1:
            return dp[i][j]


        directs = [[1, 0], [0, 1]]

        visited[i][j] = True
        minimum_sum = sys.maxsize
        for direct in directs:
            r = i + direct[0]
            c = j + direct[1]
            if r >= 0 and r < len(grid) and c >= 0 and c < len(grid[0]):
                curr = grid[i][j] + self.dfs(grid, visited, r, c, dp)
                if curr < minimum_sum:
                    minimum_sum = curr
        visited[i][j] = False
        dp[i][j] = minimum_sum
        return minimum_sum