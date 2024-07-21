import sys
class MinStack:

    def __init__(self):
        self.stack = []
        self.min = sys.maxsize

    def push(self, val: int) -> None:
        if val < self.min:
            self.min = val
        self.stack.append((val, self.min))
        
    def pop(self) -> None:
        self.stack.pop()
        if self.stack:
            self.min = self.stack[-1][1]
        else:
            self.min = sys.maxsize 

    def top(self) -> int:
        return self.stack[-1][0]

    def getMin(self) -> int:
        return self.stack[-1][1]
