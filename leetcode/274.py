# 274. H-Index
class Solution:
    def hIndex(self, citations: List[int]) -> int:

        citations.sort()
        highest = 0
        for i in range(len(citations)):
            remain = len(citations) - i
            hIndex = min(remain, citations[i])
            if hIndex > highest:
                highest = hIndex
        return highest