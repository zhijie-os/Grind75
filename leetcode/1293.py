# 1293. Shortest Path in a Grid with Obstacles Elimination
import sys 
class Solution:
    def shortestPath(self, grid: list[list[int]], k: int) -> int:
        visited = [[[sys.maxsize] * (k+1) for _ in range(len(grid[0]))] for _ in range(len(grid))]
        dp = [[[sys.maxsize for _ in range(k+1)] for _ in range(len(grid[0])) ] for _ in range(len(grid))]
        result = self.dfs(grid, visited, 0, 0, k, dp, 0)

        if result == sys.maxsize:
            return -1
        else: 
            return result

    def dfs(self, grid, visited, i, j, k, dp, pathLen):
        if pathLen > len(grid[0]) * len(grid):
            return sys.maxsize
        # base case
        if pathLen >= visited[i][j][k]:  
            return dp[i][j][k]
        if dp[i][j][k] != sys.maxsize:
            return dp[i][j][k]
        if i == len(grid)-1 and j == len(grid[0])-1:
            dp[i][j][k] = 0
            return 0
        manhatton = len(grid) - 1 - i + len(grid[0]) - 1 + j
        if k>= manhatton:
            dp[i][j][k] = manhatton
            return manhatton

        directs = [[1,0], [0,1], [0, -1], [-1, 0]]
        minStep = sys.maxsize
        visited[i][j][k] = pathLen
        for direct in directs:
            curr = sys.maxsize
            # boundary check
            if i + direct[0] >= 0 and i + direct[0] < len(grid):
                if j + direct[1] >= 0 and j + direct[1] < len(grid[0]):
                    if grid[i + direct[0]][j + direct[1]] == 1:
                        if k > 0:
                            if dp[i + direct[0]][j + direct[1]][k-1] != sys.maxsize:
                                curr = dp[i + direct[0]][j + direct[1]][k-1] + 1
                            else:
                                curr = self.dfs(grid, visited, i + direct[0], j + direct[1], k-1, dp, pathLen+1) + 1
                        else:
                            curr = sys.maxsize
                    else:
                        if dp[i + direct[0]][j + direct[1]][k] != sys.maxsize:
                            curr = dp[i + direct[0]][j + direct[1]][k] + 1
                        else:
                            curr = self.dfs(grid, visited, i + direct[0], j + direct[1], k, dp, pathLen+1) + 1
            minStep = min(minStep, curr)
        dp[i][j][k] = minStep
        return minStep

s = Solution()
result = s.shortestPath([[0,1,0,0,1,1,1,0,1,1,0,0,1,1,1,0,1],[0,1,0,0,0,0,0,1,0,0,1,0,0,1,0,1,1],[1,1,0,1,1,1,1,1,0,0,0,0,1,0,0,1,1],[0,0,0,1,1,1,1,1,0,0,1,0,1,1,1,0,1],[1,0,1,0,0,1,0,0,1,0,1,0,0,0,1,1,1],[0,0,1,0,1,0,1,0,1,0,0,1,1,1,1,1,0],[1,0,1,1,0,0,1,0,0,1,1,1,1,1,1,0,1],[0,1,1,1,1,0,0,1,0,1,1,0,0,1,1,1,0],[1,1,0,0,1,1,1,0,1,0,1,1,1,0,1,1,1],[0,0,0,1,0,1,1,1,1,1,1,1,0,0,0,0,0],[0,1,0,1,0,0,1,1,0,1,0,1,0,0,0,0,1],[1,0,1,0,1,0,1,0,0,0,1,1,1,0,0,0,1],[1,1,0,0,0,0,1,1,1,1,0,0,0,1,1,1,0],[0,0,1,1,1,1,1,1,0,1,0,0,1,1,0,1,1],[0,0,1,0,1,1,0,0,0,1,0,1,0,0,0,0,0],[0,1,1,0,1,1,0,1,1,1,0,1,0,1,1,1,1],[0,0,0,1,1,1,1,1,0,0,1,1,1,0,1,0,1],[0,1,1,0,1,0,0,0,1,1,1,0,1,1,1,0,0],[0,0,0,1,1,1,0,1,1,1,0,1,1,0,1,0,0],[0,0,1,0,0,1,0,1,1,0,0,1,0,1,1,0,0],[0,1,1,0,0,1,0,0,0,1,1,1,1,0,0,1,1],[1,0,1,0,1,0,0,0,1,0,1,0,0,0,0,0,1],[1,1,1,0,1,1,0,1,0,0,1,1,0,0,1,1,1],[1,0,0,0,1,1,0,1,1,1,0,1,1,1,1,1,0]], 38)

print(result)