// https://leetcode.com/problems/min-stack

class MinStack:

    def __init__(self):
        self.A = []
        self.S = []
    def push(self, val: int) -> None:
        self.A.append(val)
        if not self.S:
            self.S.append(val)
        else:
            self.S.append(min(val,self.S[-1]))
    def pop(self) -> None:
        self.S.pop()
        return self.A.pop()
    def top(self) -> int:
        return self.A[-1]
    def getMin(self) -> int:
        return self.S[-1]


# Your MinStack object will be instantiated and called as such:
# obj = MinStack()
# obj.push(val)
# obj.pop()
# param_3 = obj.top()
# param_4 = obj.getMin()