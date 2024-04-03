// https://leetcode.com/problems/count-sorted-vowel-strings

class Solution:
    def countVowelStrings(self, n: int) -> int:
        R = [1,1,1,1,1]
        for i in range(1,n):
            A = R
            for j in range(1,5):
                R[j] = R[j] + A[j-1]
        return sum(R)