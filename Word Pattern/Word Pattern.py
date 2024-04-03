// https://leetcode.com/problems/word-pattern

class Solution:
    def wordPattern(self, pattern: str, s: str) -> bool:
        l = s.split(' ')
        if(len(l) != len(pattern)):
            return False
        D1, D2 = {}, {}
        for i in range(len(pattern)):
            if pattern[i] not in D1:
                D1[pattern[i]] = l[i]
                D2[l[i]] = pattern[i]
        for i in range(len(pattern)):
            if not (D1[pattern[i]] == l[i] and pattern[i] == D2[l[i]]):
                return(False)
        return(True)