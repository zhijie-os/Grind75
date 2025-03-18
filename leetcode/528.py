from random import randrange
import math
class Solution:

    def __init__(self, w: list[int]):
        self.total = sum(w)
        self.pickList = []
        curr = 0
        for i in range(len(w)):
            weight = w[i]
            curr += weight
            self.pickList.append(curr)

    def pickIndex(self) -> int:
        target = randrange(self.total)
        # do a binary search
        left = 0
        right = len(self.pickList) - 1
        while left < right:
            mid = math.floor((left+right) / 2)
            if target < self.pickList[mid]:
                if mid > 0:
                    if target >= self.pickList[mid - 1]:
                        return mid
                    else:
                        right = mid - 1
                else:
                    return mid
            elif target >= self.pickList[mid]:
                left = mid + 1
        return left
                 