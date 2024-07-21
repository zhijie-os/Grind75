class Solution:
    def numIslands(self, grid: List[List[str]]) -> int:
        num_islands = 0
        def dfs(grid, i, j):
            dirs = [(1,0), (-1,0), (0, 1), (0, -1)]
            if (grid[i][j] == "1"):
                grid[i][j] = "0"
                for dir_ in dirs:
                    r = i + dir_[0]
                    c = j + dir_[1]
                    if r >= 0 and r < len(grid) and c >=0 and c < len(grid[0]):
                        dfs(grid, r, c)

        for i in range(len(grid)):
            for j in range(len(grid[0])):
                if grid[i][j] == "1":
                    dfs(grid, i, j)
                    num_islands += 1
        return num_islands
