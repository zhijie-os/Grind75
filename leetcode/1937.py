class Solution:
    def maxPoints(self, points) -> int:
        m = len(points)
        n = len(points[0])

        dp = [[0 for _ in range(n)] for _ in range(m)]
        dp[0] = points[0]
        left = [0] * n
        right = [0] * n

        for i in range(1, m): # for each row
            for j in range(n):
                if j == 0:
                    left[j] = dp[i-1][j]
                else:
                    left[j] = max(dp[i][j-1]-1, dp[i-1][j])
            for j in range(n-1, -1, -1):
                if j == n-1:
                    right[j] = dp[i-1][j]
                else:
                    right[j] = max(dp[i][j+1]-1, dp[i-1][j])

            for j in range(n):
                dp[i][j] = points[i][j] + max(left[j], right[j])

        return max(dp[m-1])
            # so what is the dp[i][j-1]
            

s = Solution()
