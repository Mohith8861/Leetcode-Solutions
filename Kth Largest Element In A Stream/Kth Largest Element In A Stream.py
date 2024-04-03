// https://leetcode.com/problems/kth-largest-element-in-a-stream

class KthLargest:
    import heapq 
    def __init__(self, k: int, nums: List[int]):
        heapq.heapify(nums)
        while(len(nums)>k):
            heapq.heappop(nums)
        self.Q = nums
        self.k = k

    def add(self, val: int) -> int:
        heapq.heappush(self.Q,val)
        if(len(self.Q) > self.k):
            heapq.heappop(self.Q)
        return self.Q[0]


# Your KthLargest object will be instantiated and called as such:
# obj = KthLargest(k, nums)
# param_1 = obj.add(val)