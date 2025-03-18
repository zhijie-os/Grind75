class Solution:
    def maxSubArray(self, nums) -> int:
        # this problem can be solved by divide and conquer
        return self.MaxSubArraySolve(nums, 0, (len(nums)-1))

    # indexing is inclusive
    def CrossSum(self, nums, left, right, mid):
        # left side longest subarray
        left_sum = nums[mid]
        max_left = left_sum
        for i in range(mid-1, left-1, -1):
            left_sum += nums[i]
            if left_sum > max_left:
                max_left = left_sum
        # do the same for right
        right_sum = nums[mid+1]
        max_right = right_sum
        for i in range(mid+2, right+1):
            right_sum += nums[i]
            if right_sum > max_right:
                max_right = right_sum
        if max_left + max_right > left_sum and max_left + max_right > right_sum:
            return max_left + max_right
        elif left_sum > right_sum:
            return left_sum
        else:
            return right_sum

    # indexing is inclusive
    def MaxSubArraySolve(self, nums, left, right):

        if left == right:
            return nums[left]

        # find the mid of the array
        mid = (left + right) // 2
        # base case
        
        left_sum = self.MaxSubArraySolve(nums, left,mid)
        right_sum = self.MaxSubArraySolve(nums, mid+1, right)
        cross_sum = self.CrossSum(nums, left, right, mid)


        if left_sum >= right_sum and left_sum >= cross_sum:
            return left_sum
        elif right_sum >= left_sum and right_sum >= cross_sum:
            return right_sum
        else:
            return cross_sum
        
nums = [-2,1,-3,4,-1,2,1,-5,4]


s = Solution()
print(s.maxSubArray(nums))