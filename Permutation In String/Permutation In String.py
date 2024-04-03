// https://leetcode.com/problems/permutation-in-string

class Solution:
    def checkInclusion(self, s1: str, s2: str) -> bool:
        d1 = [0]*26
        d2 = [0]*26
        k = len(s1)
        l = len(s2)
        if(k > l):
            return False
        for i in range(k):
            d1[ord(s1[i])-97] += 1
            d2[ord(s2[i])-97] += 1
        if(d2 == d1):
            return True
        for i in range(len(s2)-k):
            d2[ord(s2[i+k])-97] += 1
            d2[ord(s2[i])-97] -= 1
            if(d2 == d1):
                return True
        return False