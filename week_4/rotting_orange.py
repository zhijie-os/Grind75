class Solution:
    def orangesRotting(self, grid: List[List[int]]) -> int:
        bfs = []
        num_unrotten = 0

        for i in range(len(grid)):
            for j in range(len(grid[0])):
                if grid[i][j] == 1:
                    num_unrotten += 1
                elif grid[i][j] == 2:
                    bfs.append((i,j))

        turn = 0
        dirs = [(1, 0), (-1, 0), (0, 1), (0, -1)]

        while bfs:
            turn += 1
            next_ = []
            for e in bfs:
                for dir_ in dirs:
                    r = e[0] + dir_[0]
                    c = e[1] + dir_[1]
                    if r >= 0 and r < len(grid) and c >= 0 and c < len(grid[0]) and grid[r][c] == 1:
                        grid[r][c] = 2
                        num_unrotten -= 1
                        next_.append((r, c))
            bfs = next_
        
        if num_unrotten > 0:
            return -1
        elif turn == 0:
            return 0
        else:
            return turn - 1


s = Solution()
print(s.orangesRotting([[2,1,1],[1,1,0],[0,1,1]]))