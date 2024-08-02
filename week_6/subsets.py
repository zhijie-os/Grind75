class Solution:
    def subsets(self, nums: List[int]) -> List[List[int]]:
        acc = []
        self.subsets_helper(nums, 0,  [], acc)
        return acc

    def subsets_helper(self, nums, count, carry, acc):
        result = carry

        if count == len(nums):
            return acc.append(result)
        
        self.subsets_helper(nums, count+1, carry+[nums[count]], acc)
        self.subsets_helper(nums, count+1, carry, acc)
        
