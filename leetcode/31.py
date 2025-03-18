# 31. Next Permutation
class Solution:
    def nextPermutation(self, nums: List[int]) -> None:
        """
            Find the largest index k such that a[k] < a[k + 1]. If no such index exists, the permutation is the last permutation.
            Find the largest index l greater than k such that a[k] < a[l].
            Swap the value of a[k] with that of a[l].
            Reverse the sequence from a[k + 1] up to and including the final element a[n].
        """
        k = -1
        l = -1
        for i in range(len(nums)-1):
            if nums[i] < nums[i+1]:
                k = i
        if k == -1:
            nums.sort()
            return nums
        for i in range(len(nums)):
            if nums[i] > nums[k]:
                l = i

        print(k, l)
        tmp = nums[k]
        nums[k] = nums[l]
        nums[l] = tmp
        nums[k+1:] = nums[k+1:][::-1] 
        return nums

