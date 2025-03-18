# 63. Unique Path II
class Solution:
    def uniquePathsWithObstacles(self, obstacleGrid: List[List[int]]) -> int:
        visited = [[False for _ in range(len(obstacleGrid[0]))] for _ in range(len(obstacleGrid))]
        dp = [[0 for _ in range(len(obstacleGrid[0]))] for _ in range(len(obstacleGrid))]
        return self.dfs(obstacleGrid, visited, 0, 0, dp)

    def dfs(self, grid, visited, i, j, dp):
        if grid[i][j] == 1:
            return 0
        if visited[i][j]:
            return 0
        if i == len(grid) - 1 and j == len(grid[0]) - 1:
            return 1
        if dp[i][j] != 0:
            return dp[i][j]

        visited[i][j] = True
        directs = [[1, 0], [0, 1]]
        acc = 0
        for direct in directs:
            r = i + direct[0]
            c = j + direct[1]
            if r >= 0 and r < len(grid) and c >= 0 and c < len(grid[0]):
                acc += self.dfs(grid, visited, r, c, dp)
        visited[i][j] = False
        dp[i][j] = acc
        return acc