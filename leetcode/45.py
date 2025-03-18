# 45. Jump Game II
class Solution:
    def jump(self, nums: List[int]) -> int:
        dp = [99999 for _ in range(len(nums)+1)]
        dp[len(nums)] = 0
        dp[len(nums)-1] = 0
        return self.jumpDP(nums, 0, dp)
    
    def jumpDP(self, nums, pos, dp):
        if pos >= len(nums) - 1:
            return 0
        if dp[pos] != 99999:
            return dp[pos]
        
        smallest = 99999
        for i in range(1, nums[pos]+1):
            curr_jump = self.jumpDP(nums, pos+i, dp) + 1
            if curr_jump < smallest:
                smallest = curr_jump
        dp[pos] = smallest
        return smallest