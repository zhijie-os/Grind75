class Solution:
    def fourSum(self, nums: List[int], target: int) -> List[List[int]]:
        nums.sort()
        res = []

        for i, a in enumerate(nums):
            threes = self.threeSum(nums[i+1:], target-a)
            for e in threes:
                toAppend = [a]
                toAppend.extend(e)
                if toAppend not in res:
                    res.append(toAppend)
        return res


    def threeSum(self, nums, target):
        res = []
        print(nums)
        for i, a in enumerate(nums):
            l = i + 1
            r = len(nums) - 1

            while l < r:
                threeSum = a + nums[l] + nums[r]
                if threeSum == target:
                    res.append([a, nums[l], nums[r]])
                if threeSum > target:
                    r -= 1
                else:
                    l += 1
            
        return res