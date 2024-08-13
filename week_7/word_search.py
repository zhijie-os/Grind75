class Solution:
    def exist(self, board: List[List[str]], word: str) -> bool:
        m = len(board)
        n = len(board[0])

        for i in range(m):
            for j in range(n):
                if self.exist_helper(board, word, i, j, []):
                    return True
        return False

    def exist_helper(self, board, word, i, j, history):
        if len(word) == 1:
            return board[i][j] == word[0]
        if word == '':
            return True
        if word[0] != board[i][j]:
            return False
        m = len(board)
        n = len(board[0])
        directions = {(1,0), (-1,0), (0, 1), (0, -1)}
        for direction in directions:
            row = i + direction[0]
            col = j + direction[1]
            if (row, col) not in history and  row >= 0 and row < m and col >= 0 and col < n and self.exist_helper(board,word[1::], row, col, history+[(i,j)]):
                return True
        return False