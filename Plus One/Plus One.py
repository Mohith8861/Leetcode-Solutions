// https://leetcode.com/problems/plus-one

class Solution:
    def plusOne(self, digits: List[int]) -> List[int]:
        t = 0
        for g in range(0,len(digits)):
            t += digits[::-1][g] * (10 ** g)
        t = t + 1
        digits = [int(x) for x in str(t)]
        return digits