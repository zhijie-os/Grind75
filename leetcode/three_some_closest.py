class Solution:
    def threeSumClosest(self, nums: List[int], target: int) -> int:
        res = float('inf')
        nums.sort()

        for i,a in enumerate(nums):
            l = i + 1
            r = len(nums) - 1
            while l < r:
                threeSum = a + nums[l] + nums[r]
                if abs(threeSum-target) < abs(res-target):
                    res = threeSum
                if threeSum > target:
                    r -= 1
                else:
                    l += 1
        return res