class Solution:
    def uniquePaths(self, m: int, n: int) -> int:
        dp = [[ -1 for _ in range(n+1)] for _ in range(m+1)]
        dp[m][n] = 1
        return self.unique_paths_helper(m, n, 1, 1, dp)    
    
    def unique_paths_helper(self, m, n, i, j, dp):
        if i >= 1 and i <= m and j >= 1 and j <= n:
            if i == m and j == n:
                return 1
            if dp[i][j] != -1:
                return dp[i][j]
            if  i+1 <= m and dp[i+1][j] != -1:
                go_down = dp[i+1][j]
            else:
                go_down = self.unique_paths_helper(m, n, i+1, j, dp) 
            if  j + 1 <= n and dp[i][j+1] != -1:
                go_right = dp[i][j+1]
            else:
                go_right = self.unique_paths_helper(m, n, i, j + 1, dp)
            dp[i][j] = go_down + go_right
            return go_down + go_right
        else:
            return 0
