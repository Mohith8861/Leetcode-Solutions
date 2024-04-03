// https://leetcode.com/problems/smallest-range-covering-elements-from-k-lists

class Solution:
    def smallestRange(self, nums: List[List[int]]) -> List[int]:
        L = float('inf')
        k = len(nums)
        for i in range(k):
            L = min(len(nums[i]), L)
        if(L == 1 and k == 1):
            return[nums[0][0],nums[0][0]]
        import heapq
        A = [-1e9, 1e9]
        H = []
        j = 0
        a = -100
        for i in range(k):
            a = nums[i].pop(0)
            heapq.heappush(H, (a, i))
        y = heapq.heappop(H)
        l, X = heapq.nlargest(1, H)[0][0], y[0]
        if (A[1] - A[0] > l - X):
            A[0] = X
            A[1] = l
        j = y[1]
       
        while nums[j]:
            a = nums[j].pop(0)
            heapq.heappush(H, (a, j))
            y = heapq.heappop(H)
            l, X = heapq.nlargest(1, H)[0][0], y[0]
            if (A[1] - A[0] > l - X):
                A[0] = X
                A[1] = l
            j = y[1]
        return(A)