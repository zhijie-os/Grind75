# 153. Find Minimum in Rotated Sorted Array
class Solution:
    def findMin(self, nums: List[int]) -> int:
        if len(nums) == 1:
            return nums[0]

        if nums[0] < nums[len(nums)-1]:
            return nums[0]
        
        left = 0
        right = len(nums) - 1
        last = nums[0]
        while left <= right:
            mid = (left + right) // 2
            print(mid, nums[mid])
            if nums[mid - 1] > nums[mid]:
                return nums[mid]
            else:
                if last > nums[mid]:
                    right = mid -1
                else:
                    left = mid + 1
            last = nums[mid]
        return -1


