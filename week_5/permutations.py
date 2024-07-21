class Solution:
    def permute(self, nums: List[int]) -> List[List[int]]:
        res = []

        if len(nums) == 1:
            return [nums.copy()]
        
        for i in range(len(nums)):
            # chose one
            n = nums.pop(0)
            perms = self.permute(nums)
            for p in perms:
                p.append(n)
                res.append(p.copy())

            # reverse the chose
            nums.append(n)
        
        return res