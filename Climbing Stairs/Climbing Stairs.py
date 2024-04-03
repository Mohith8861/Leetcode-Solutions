// https://leetcode.com/problems/climbing-stairs

class Solution:
    def climbStairs(self, n: int) -> int:
        #DP version is practically fibonacci problem
        if(n == 1):
            return 1
        o , t  = 1 , 1 
        r = 0
        for i in range(n-1):
            r = t + o
            o = t
            t = r
        return r
