// https://leetcode.com/problems/best-time-to-buy-and-sell-stock

class Solution:
    def maxProfit(self, p: List[int]) -> int:
        l = len(p)
        m = 0
        e = p[0]
        for i in range(1,l):
            if(e > p[i]):
                e = p[i]
            if(p[i] - e > m):
                m = p[i] - e
        return(m)