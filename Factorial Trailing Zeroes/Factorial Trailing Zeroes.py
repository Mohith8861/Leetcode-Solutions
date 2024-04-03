// https://leetcode.com/problems/factorial-trailing-zeroes

class Solution:
    def trailingZeroes(self, n: int) -> int:
        if(n < 5):
            return 0
        j = 0
        for i in range(5,n+1):
            if((i % 5 == 0)):
                while (i % 5 == 0):
                    j += 1
                    i = i // 5
        return j