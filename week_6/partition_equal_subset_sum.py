class Solution:
    def canPartition(self, nums: List[int]) -> bool:
        if sum(nums)%2 != 0:
            return False

        dp = [[-1 for _ in range(sum(nums)+1)] for _ in range(len(nums))]
        for i in range(len(nums)):
            dp[i][sum(nums)//2] = True
        return self.can_partition(nums, 0, 0, sum(nums)//2, dp)

    def can_partition(self, nums, index, sum_, target, dp):
        if sum_ == target:
            return True
        if len(nums) == index + 1:
            return sum_ + nums[index] == target
        if index >= len(nums):
            return False  
        a = False
        b = False
        if dp[index+1][sum_+nums[index]] != -1:
            a = dp[index+1][sum_+nums[index]]
        else:
            a = self.can_partition(nums, index + 1, sum_ + nums[index], target, dp)


        if dp[index+1][sum_] != -1:
            b = dp[index+1][sum_]
        else:
            b = self.can_partition(nums, index + 1, sum_ , target, dp)


        dp[index][sum_] = a or b
        return a or b