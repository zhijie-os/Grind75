class Solution:
    def maxSubArray(self, nums) -> int:
        # one question to answer is that what is the subproblem in this case for DP?
        # the subproblem is dp[i] = the maximum subarrary from 0 to i
        dp = [0] * len(nums)
        dp[0] = nums[0]
        max_sub = -float('inf')
        for i in range(1, len(nums)):
            # it is either include or exclude and restart the counting
            # include 
            if nums[i] >= 0:
                dp[i] = dp[i-1] + nums[i]
            else:
                dp[i] = dp[i-1]
            if max_sub < dp[i]:
                max_sub = dp[i]
        return max_sub
    