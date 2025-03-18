# 295. Find median from Data Stream
class MedianFinder:

    def __init__(self):
        self.data = []
        

    def addNum(self, num: int) -> None:
        if len(self.data) == 0:
            self.data.append(num)
            return
        if self.data[0] > num:
            self.data.insert(0, num)
        elif self.data[len(self.data)-1] < num:
            self.data.append(num)
        else:
            for i in range(len(self.data) - 1):
                if num >= self.data[i] and num <= self.data[i+1]:
                    self.data.insert(i+1, num)
                    return


    def findMedian(self) -> float:
        if len(self.data) == 0:
            return None
        else:
            length = len(self.data)
            if length % 2 == 0:
                return (self.data[length//2 - 1] + self.data[length//2]) / 2
            else:
                return self.data[len(self.data)//2]
        


# Your MedianFinder object will be instantiated and called as such:
# obj = MedianFinder()
# obj.addNum(num)
# param_2 = obj.findMedian()