// https://leetcode.com/problems/design-circular-queue

class MyCircularQueue:

    def __init__(self, k: int):
        self.Q = [-1]*k
        self.front = -1
        self.rear =  -1
        self.k = k
        self.size = 0
    def enQueue(self, value: int) -> bool:
        if self.isFull():
            return False
        elif self.isEmpty():
            self.front = self.rear = 0
            self.Q[self.front] = value
            self.size += 1
            return True
        else:
            self.rear = (self.rear + 1) % (self.k)
            self.Q[self.rear] = value
            self.size += 1
            return True

    def deQueue(self) -> bool:
        if self.isEmpty():
            return False
        elif(self.size == 1):
            self.Q[self.front] = -1
            self.front = -1
            self.rear =  -1
            self.size -= 1
            return True
        else:
            self.Q[self.front] = -1
            self.front = (self.front + 1) % (self.k)
            self.size -= 1
            return True

    def Front(self) -> int:
        return self.Q[self.front]

    def Rear(self) -> int:
        return self.Q[self.rear]

    def isEmpty(self) -> bool:
        return self.size == 0

    def isFull(self) -> bool:
        return self.size == self.k


# Your MyCircularQueue object will be instantiated and called as such:
# obj = MyCircularQueue(k)
# param_1 = obj.enQueue(value)
# param_2 = obj.deQueue()
# param_3 = obj.Front()
# param_4 = obj.Rear()
# param_5 = obj.isEmpty()
# param_6 = obj.isFull()