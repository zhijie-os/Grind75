class Solution:
    def rob(self, nums: List[int]) -> int:
        # for each house rob or not rob 
        # if robbed, skip one house - required
        dp = [[[-1 for _ in range(2) ] for _ in range(2)] for _ in range(len(nums))]
        return self.rob_helper(0, nums, False, False, dp)
    
    def rob_helper(self, index, nums, robbed, first, dp):
        # base case 
        # last house, only rob or not rob
        if index == len(nums) - 1:
            if robbed or first:
                dp[index][robbed][first] = 0
                return 0
            else:
                dp[index][robbed][first] = nums[index]
                return nums[index]
        # at index i, return the max, either rob this house or not 
        a = 0 

        if not robbed:    # can rob nums[i] + dp[i+1]
            if index == 0:
                if dp[index+1][1][1] != -1:
                    a = nums[index] + dp[index+1][1][1] 
                else:
                    a = nums[index] + self.rob_helper(index+1, nums, True, True, dp)
            else:
                if dp[index+1][1][first] != -1:
                    a = nums[index] + dp[index+1][1][first]
                else:
                    a = nums[index] + self.rob_helper(index+1, nums, True, first, dp)

        if dp[index+1][0][first] != -1:
            b = dp[index+1][0][first]
        else:
            b = self.rob_helper(index+1, nums, False, first, dp) # skip this house
        
        dp[index][robbed][first] = max(a,b)
        return max(a, b)
        