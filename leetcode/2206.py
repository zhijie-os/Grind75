# 2206. Divide Array Into Equal Pairs

class Solution:
    def divideArray(self, nums: List[int]) -> bool:
        freq_count = {}
        for num in nums:
            if num not in freq_count:
                freq_count[num] = 1
            else:
                freq_count[num] += 1
        
        for k, v in freq_count.items():
            if v % 2 != 0:
                return False
        
        return True