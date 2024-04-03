// https://leetcode.com/problems/implement-stack-using-queues

class MyStack:

    def __init__(self):
        self.Q = []

    def push(self, x: int) -> None:
        self.Q.append(x)

    def pop(self) -> int:
        s = []
        for i in range(len(self.Q)):
            if len(self.Q) == 1:
                break
            s.append(self.Q.pop(0))
        x = self.Q.pop(0)
        for i in range(len(s)):
            self.Q.append(s.pop(0))
        return x
    def top(self) -> int:
        return self.Q[-1]
        

    def empty(self) -> bool:
        return len(self.Q)== 0


# Your MyStack object will be instantiated and called as such:
# obj = MyStack()
# obj.push(x)
# param_2 = obj.pop()
# param_3 = obj.top()
# param_4 = obj.empty()