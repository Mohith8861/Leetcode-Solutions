// https://leetcode.com/problems/happy-number

class Solution:
    def isHappy(self, n: int) -> bool:
        S = set()
        X = n
        S.add(n)
        while(X != 1):
            L = X
            X = 0
            for i in str(L):
                X += int(i)**2
            if X not in S:
                S.add(X)
            else:
                return False
        return True