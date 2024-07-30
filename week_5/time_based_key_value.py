class TimeMap:

    def __init__(self):
        self.map = {}

    def set(self, key: str, value: str, timestamp: int) -> None:
        if key in self.map:
            self.map[key].append((value, timestamp))
        else:
            self.map[key] = [(value, timestamp)]

    def get(self, key: str, timestamp: int) -> str:
        res = ""
        if key in self.map:
            arr = self.map[key]
        else:
            arr = []
        l = 0
        r = len(arr)-1
        while l <= r:
            mid = (l+r)//2
            if arr[mid][1] <= timestamp:
                l = mid + 1
                res = arr[mid][0]
            else:
                r = mid - 1
        return res

