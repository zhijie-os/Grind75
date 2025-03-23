# 209. Minimum Size Subarray Sum
class Solution:
    def minSubArrayLen(self, target: int, nums: List[int]) -> int:
        if not nums:
            return 0

        left = 0
        right = 0
        acc = 0
        k = sys.maxsize
        for i in range(len(nums)):
            acc += nums[i]
            right = i
            while acc >= target:
                k = min(right - left + 1, k)
                acc -= nums[left]
                left += 1
        
        if k == sys.maxsize:
            return 0
        else:
            return k