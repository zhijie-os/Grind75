class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        # can calculate prefix in O(n)
        prefix = [ 0 for _ in range(len(nums))]
        accumulate = 1
        for i in range(len(nums)):
            prefix[i] = accumulate
            accumulate *= nums[i]
        
        # can calculate suffix in O(n)
        suffix = [ 0 for _ in range(len(nums))]
        accumulate = 1
        for i in range(len(nums)-1, -1, -1):
            suffix[i] = accumulate
            accumulate *= nums[i]
        
        # result = prefix * suffix
        result = []
        for i in range(len(nums)):
            result.append(prefix[i]*suffix[i])
        return result

s = Solution()
print(s.productExceptSelf([1,2,3,4]))