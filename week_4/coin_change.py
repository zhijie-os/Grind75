import sys
class Solution:
    def coinChange(self, coins, amount: int) -> int:
        dp = [-1 for i in range(amount+1)]
        for c in coins:
            dp[c] = 1
        dp[0] = 0
        coins.sort()
        for i in range(1, amount+1):
            dp[i] = sys.maxsize
            for c in coins:
                if (i < c):
                    break
                if dp[i-c] != sys.maxsize:
                    dp[i] = min(dp[i],dp[i-c] + 1)
        if dp[amount] == sys.maxsize:
            return -1
        else:
            return dp[amount]

s = Solution()
print(s.coinChange([1,2,5], 11))