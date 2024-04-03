// https://leetcode.com/problems/palindromic-substrings

class Solution:
    def countSubstrings(self, s: str) -> int:
        A = 0
        for k in range(len(s)):
            i, j = k, k
            while (i >= 0 and j < len(s) and s[j] == s[i]):
                A +=1
                i -= 1
                j += 1
            i, j = k, k + 1
            while (i >= 0 and j < len(s) and s[j] == s[i]):
                A +=1
                i -= 1
                j += 1
        return A