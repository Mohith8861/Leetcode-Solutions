// https://leetcode.com/problems/kth-largest-element-in-an-array

import heapq
class Solution:
    def findKthLargest(self, nums: List[int], k: int) -> int:
        heapq.heapify(nums)
        a = 0
        for i in range(len(nums)-k+1):
            a = heapq.heappop(nums)
        return a