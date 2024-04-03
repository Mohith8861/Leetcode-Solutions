// https://leetcode.com/problems/minimum-number-of-swaps-to-make-the-string-balanced

class Solution:
    def minSwaps(self, s: str) -> int:
        st = []
        close = 0
        max1 = 0
        for i in s:
            if i == '[':
                close -= 1
            else:
                close += 1
            max1 = max(max1,close)
        return (max1+1)//2