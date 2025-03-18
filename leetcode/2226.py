# 2226. Maximum Candies Allocated to K Children
class Solution:
    def maximumCandies(self, candies: List[int], k: int) -> int:
        totalCandies = sum(candies)
        idealResult = totalCandies // k
        if idealResult == 0:
            return idealResult
        print(idealResult)
        left = 1
        right = idealResult
        maximumCanGet = 1
        while left <= right:
            mid = (left + right) // 2

            can_split = 0
            for pile in candies:
                can_split += pile//mid
            
            
            if can_split >= k:
                maximumCanGet = max(mid, maximumCanGet)
                left = mid + 1
            else:
                right = mid - 1
        return maximumCanGet