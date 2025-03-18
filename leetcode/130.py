# 130. Surrounded Regions
class Solution:
    def solve(self, board: List[List[str]]) -> None:
        """
        Do not return anything, modify board in-place instead.
        """
        for i in range(len(board)):
            for j in range(len(board[0])):
                if board[i][j] == 'X':
                    continue
                visited = [[ False for _ in range(len(board[0]))] for _ in range(len(board))]
                if board[i][j] == 'O' and self.surrounded(board, i, j, visited):
                    visited = [[ False for _ in range(len(board[0]))] for _ in range(len(board))]
                    self.flipGrid(board, i, j, visited)

    
    def flipGrid(self, board, i, j,visited):
        if visited[i][j]:
            return
        if board[i][j] == 'O':
            board[i][j] = 'X'
        else: # if reached 'X' stop
            return
        
        directs = [[1, 0,], [0, 1], [-1, 0], [0, -1]]
        visited[i][j] = True
        for direct in directs:
            r = i + direct[0]
            c = j + direct[1]
            if r >= 0 and r < len(board) and c >= 0 and c < len(board[0]):
                self.flipGrid(board, r, c, visited)

    
    def surrounded(self, board, i, j, visited):
        if visited[i][j]:
            return True
        if board[i][j] == 'X':
            return True
        if i == 0 or i == len(board) - 1 or j == 0 or j == len(board[0]) - 1:
            return False

        directs = [[1, 0,], [0, 1], [-1, 0], [0, -1]]
        visited[i][j] = True
        for direct in directs:
            r = i + direct[0]
            c = j + direct[1]
            if r >= 0 and r < len(board) and c >= 0 and c < len(board[0]):
                if not self.surrounded(board, r, c, visited):
                    return False
        return True
            