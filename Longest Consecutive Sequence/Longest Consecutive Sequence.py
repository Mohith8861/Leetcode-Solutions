// https://leetcode.com/problems/longest-consecutive-sequence

class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        import heapq
        R = []
        r = 0
        heapq.heapify(nums)
        for i in range(len(nums)):
            if not R:
                R.append(heapq.heappop(nums))
            if nums: 
                x = heapq.heappop(nums)
                if R[-1] + 1 == x:
                    R.append(x)
                elif R[-1] == x:
                    continue
                else:
                    heapq.heappush(nums, x)
                    r = max(r,len(R))
                    R.clear()
        if R:
            r = max(len(R),r)
        return r