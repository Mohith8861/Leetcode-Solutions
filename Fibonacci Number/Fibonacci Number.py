// https://leetcode.com/problems/fibonacci-number

class Solution:
    def fib(self, n: int) -> int:
        if(n == 0):
            return n
        if(n == 1 or n == 2):
            return 1
        D1,D2 = 1,1
        D3 = 0
        for i in range(3,n+1):
            D3 = D1 + D2
            D1 = D2
            D2 = D3
        return D3