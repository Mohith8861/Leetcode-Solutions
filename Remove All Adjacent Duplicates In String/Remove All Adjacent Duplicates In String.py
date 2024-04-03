// https://leetcode.com/problems/remove-all-adjacent-duplicates-in-string

class Solution:
    def removeDuplicates(self, s: str) -> str:
        S = []
        for i in range(len(s)):
            if((not S) or S[-1] != s[i]):
                S.append(s[i])
            elif(S[-1] == s[i]):
                S.pop()
        r = ''
        while(S):
            r += S.pop(0)
        return r