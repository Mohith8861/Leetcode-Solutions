// https://leetcode.com/problems/reverse-integer

class Solution:
    def reverse(self, x: int) -> int:
        a = 0
        f = False
        if(x < 0):
            x = abs(x)
            f = True
        while (x != 0):
            a = (a*10) + (x % 10)
            x = x // 10
        if(-2**31 > a or a > (2**31 - 1)):
            return 0
        if(f):
            return -a
        return a
        