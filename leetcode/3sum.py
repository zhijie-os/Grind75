class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        # use two pointers
        ans = set()
        nums.sort()
        

        # used two pointers that solved two sum II
        for i in range(len(nums)):
            left = i + 1
            right = len(nums) - 1
            target = -nums[i]
            while left < right:
                if nums[left] + nums[right] == target:
                    ans.add((nums[i], nums[left], nums[right]))
                    left += 1
                    right -= 1
                elif nums[left] + nums[right] < target:
                    left += 1
                else:
                    right -= 1
        return list(ans)