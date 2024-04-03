// https://leetcode.com/problems/trapping-rain-water

class Solution:
    def trap(self, height: List[int]) -> int:
        n = len(height)
        l,r = [0 for i in range(n)],[0 for j in range(n)]
        res = 0
        l[0] = 0
        for i in range(1,n):
            l[i] = max(l[i-1],height[i-1])
        r[n-1] = 0
        for j in range(n-2,-1,-1):
            r[j] = max(r[j+1],height[j+1])
        for k in range(n):
            o = min(l[k],r[k]) - height[k]
            if(o > 0):
                res += o 
        return res