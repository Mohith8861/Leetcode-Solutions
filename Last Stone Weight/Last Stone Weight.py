// https://leetcode.com/problems/last-stone-weight

class Solution:
    def lastStoneWeight(self, stones: List[int]) -> int:
        if(len(stones) == 1):
            return stones[0]
        import heapq
        stones = [-i for i in stones.copy()]
        heapq.heapify(stones)
        
        while(stones and len(stones) > 1):
            a,b = heapq.heappop(stones), heapq.heappop(stones)
            if(a==b):
                continue
            else:
                heapq.heappush(stones,-abs(a-b))
        if(not stones):
            return 0
        return stones[0]*-1
